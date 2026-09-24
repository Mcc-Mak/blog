import { useState } from "react";
import { NavLink } from "react-router-dom";

const navLinks = [
  { to: "/", label: "Home", icon: "\u2694", xp: 50 },
  { to: "/projects", label: "Projects", icon: "\uD83E\uDDF0", xp: 60 },
  { to: "/gallery", label: "Gallery", icon: "\uD83C\uDFF0", xp: 80 },
];

function Navbar({ xp, addXp }) {
  const [xpPop, setXpPop] = useState(null);

  const handleNavClick = (index) => {
    setXpPop(index);
    addXp(navLinks[index].xp);
    setTimeout(() => setXpPop(null), 400);
  };

  return (
    <nav className="navbar">
      <div className="nav-links">
        {navLinks.map((link, index) => (
          <NavLink
            key={link.to}
            to={link.to}
            end={link.to === "/"}
            className={({ isActive }) => (isActive ? "nav-item active" : "nav-item")}
            onClick={() => handleNavClick(index)}
          >
            <span className="nav-icon">{link.icon}</span>
            <span className="nav-label">{link.label}</span>
            {xpPop === index && <span className="xp-fly">+{link.xp}XP</span>}
          </NavLink>
        ))}
      </div>
      <div className="nav-xp">
        <span className="xp-icon">&#11088;</span>
        <span className="xp-value">{xp}</span>
        <span className="xp-label">XP to Know Me</span>
      </div>
    </nav>
  );
}

export default Navbar;