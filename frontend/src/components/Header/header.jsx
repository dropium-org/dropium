import React from "react";
import "./header.css";
import logo from "../../assets/header/logo-dropium.svg";

const Header = ({ menu , buttonBox, ...props}) => {
  return (
    <div className="header-wrapper">
      <header {...props}>
        <div className="header-logo">
          <img src={logo} alt="logo" height={"15%"} />
        </div>
        {menu && <div className="header-menu">{menu}</div>}
        {buttonBox && <div className="header-button-box">{buttonBox}</div>}
      </header>
    </div>
  );
};

export default Header;
