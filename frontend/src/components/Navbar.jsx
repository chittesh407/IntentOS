import logo from "../assets/Logo.jpeg";
function Navbar() {
  return (
    <nav className="navbar">
      <div className="logo">
        <img src={logo} alt="IntentOS" className="logo-img" />
        <span>IntentOS</span>
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