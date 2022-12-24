import React, { useState } from "react";
import "./dropium-panel.css";

const DropiumPanel = ({
  children,
  title,
  startIcon,
  endIcon,
  contentStyle,
  ...props
}) => {
  const [show, setShow] = useState(false);
  const onClick = (e) => {
    e.preventDefault();
    setShow((cur) => !cur);
  };
  return (
    <div className="dropium-panel-wrapper" {...props}>
      <a
        href="/#"
        onClick={onClick}
        className={`panel-title ${show ? "active" : ""}`}
      >
        {startIcon && (
          <i className="start-icon" style={{ width: "24px", height: "24px" }}>
            {startIcon}
          </i>
        )}
        <span>{title}</span>
        {endIcon && (
          <i className="end-icon" style={{ width: "24px", height: "24px" }}>
            {endIcon}
          </i>
        )}
      </a>
      {!show ? (
        <div className="panel-content panel-shadow"></div>
      ) : (
        <div className="panel-content dropdown-content-wrapper">
          <div className="dropdown-content" style={contentStyle}>
            {children}
          </div>
        </div>
      )}
    </div>
  );
};

export default DropiumPanel;
