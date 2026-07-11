function Navbar() {
  return (
    <nav className="navbar">
      <div className="logo">
        🧠 <span>IntentOS</span>
      </div>

      <div className="navbar-right">
        <div className="status">
          <span className="status-dot"></span>
          Local AI
        </div>

        <button className="settings-btn">
          ⚙️
        </button>
      </div>
    </nav>
  );
}

export default Navbar;