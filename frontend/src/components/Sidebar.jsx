function Sidebar() {
  return (
    <aside className="sidebar">
      <button className="new-chat-btn">
        + New Chat
      </button>

      <div className="chat-history">
        <h3>Recent Chats</h3>

        <div className="chat-item">💬 Install Python</div>
        <div className="chat-item">💬 Open VS Code</div>
        <div className="chat-item">💬 Show System Info</div>
      </div>
    </aside>
  );
}

export default Sidebar;