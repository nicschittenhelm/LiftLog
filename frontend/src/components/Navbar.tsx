import React from "react";
import '../styles/component-styles/Navbar.scss';

const  Navbar = () => {
    return (
      <div className="wrapper">
        <h1><span>Lift</span>Log</h1>
        <a>Link1</a>
        <a>Link2</a>
        <a>Link3</a>
        <a>Link4</a>
      </div>
    );
  }

export default Navbar;