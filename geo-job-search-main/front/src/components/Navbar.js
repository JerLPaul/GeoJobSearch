import React from 'react';
import { Link } from 'react-router-dom';
import logo from './logo.png';
import './Navbar.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      <img src={logo} alt="GeoJob Search Logo" style={{ width: '250px', height: 'auto' }} />
      <div className="navbar-buttons">
        <Link to="/login">Login</Link>
        <Link to="/signup">Signup</Link>
      </div>
    </nav>
  );
};

export default Navbar;
