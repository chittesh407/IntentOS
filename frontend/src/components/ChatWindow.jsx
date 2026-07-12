import logo from "../assets/Logo.jpeg";
import Message from "./Message";
import { useEffect, useRef } from "react";


function ChatWindow({ messages }) {
  const bottomRef = useRef(null);

useEffect(() => {
  bottomRef.current?.scrollIntoView({
    behavior: "smooth",
    block: "end",
  });
}, [messages.length]);
  if (messages.length === 0) {
    return (
      <div className="chat-window">
        <div className="welcome-screen">
          <div className="robot">
            <img src={logo} className="welcome-logo" alt="IntentOS Logo" />
          </div>

          <h1>Welcome to IntentOS</h1>

          <p>
            I can understand your requests,
            execute desktop tasks safely,
            and explain every action.
          </p>

          <span>How can I help you today?</span>
        </div>
      </div>
    );
  }

  return (
    <div className="chat-window messages-container">
      {messages.map((msg) => (
        <Message
          key={msg.id}
          message={msg}
        />
      ))}
      <div ref={bottomRef}></div>
    </div>
    
  );
}

export default ChatWindow;