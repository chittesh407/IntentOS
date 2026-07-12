import { useState } from "react";

function ChatInput({ onSend }) {

  const [input, setInput] = useState("");

  const handleSend = () => {

    if (input.trim() === "") return;

    onSend(input);

    setInput("");

  };

  return (

    <div className="chat-input-container">

      <input
        className="chat-input"
        type="text"
        placeholder="Ask IntentOS anything..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            handleSend();
          }
        }}
      />

      <button
        className="send-btn"
        onClick={handleSend}
      >
        ➜
      </button>

    </div>

  );

}

export default ChatInput;