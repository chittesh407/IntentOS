import { useState } from "react";

import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import ChatWindow from "./components/ChatWindow";
import ChatInput from "./components/ChatInput";

import { sendMessage } from "./services/api";

function App() {
  const [messages, setMessages] = useState([]);
  async function typeMessage(id, fullText) {
  let current = "";

  for (let i = 0; i < fullText.length; i++) {
    current += fullText[i];

    setMessages((prev) =>
      prev.map((msg) =>
        msg.id === id
          ? {
              ...msg,
              content: current,
            }
          : msg
      )
    );

    await new Promise((resolve) => setTimeout(resolve, 8));
  }

  setMessages((prev) =>
    prev.map((msg) =>
      msg.id === id
        ? {
            ...msg,
            loading: false,
          }
        : msg
    )
  );
}

  async function handleSend(message) {

    // Show user message immediately
    setMessages((prev) => [
      ...prev,
      {
        id: Date.now() + 1,
        role: "user",
        loading: false,
        content: message,
      },
    ]);

    try {

      const loadingId = Date.now();
      setMessages((prev) => [
       ...prev,
       {
        id: loadingId,
        role: "assistant",
        loading: true,
        content: "",
      },
      ]);
      const data = await sendMessage(message);

// Replace loading message
setMessages((prev) =>
  prev.map((msg) =>
    msg.id === loadingId
      ? {
          ...msg,
          loading: false,
          content: "",
        }
      : msg
  )
);

await typeMessage(loadingId, data.response);


    } catch (error) {

      setMessages((prev) => [
        ...prev,
        {
  id: Date.now(),
  role: "system",
  loading: false,
  content: "Backend connection failed ❌",
},
      ]);

      console.error(error);
    }
  }

  return (
    <>
      <Navbar />

      <div className="app-layout">

        <Sidebar />

        <div className="main-content">

          <ChatWindow messages={messages} />

          <ChatInput onSend={handleSend} />

        </div>

      </div>
    </>
  );
}

export default App;