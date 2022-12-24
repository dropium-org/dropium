import React from "react";
import "./dropium-button.css";

const DropiumButton = ({
  disableShadow = false,
  startIcon,
  endIcon,
  disabled,
  children,
  activeEffectDisabled = false,
  hoverEffectDisabled = false,
  onButtonClicked,
  style,
  shadowStyle,
  borderSide = "left" | "right" | "both",
}) => {
  const borderRadiusMap = {
    left: "999px 0px 0px 999px",
    right: "0px 999px 999px 0px ",
    both: "999px",
    none: "0px 0px 0px 0px",
  };

  return (
    <div
      disabled={disabled}
      className={`dropium-btn ${hoverEffectDisabled ? "" : "hover"} ${
        activeEffectDisabled ? "" : "activable"
      }`}
      style={{
        borderRadius: borderRadiusMap[borderSide] || borderRadiusMap["both"],
        color: "white",
        backgroundColor: "#ff2f61",
        width: "7.5em",
        height: "1em",
        padding: ".5rem",
        outline: "4px solid #000000",
        ...style,
      }}
    >
      <a
        href=""
        onClick={(e) => {
          e.preventDefault();
          onButtonClicked?.(e);
        }}
      >
        {startIcon && (
          <i className="start-icon" style={{ width: "24px", height: "24px" }}>
            {startIcon}
          </i>
        )}
        {children}
        {endIcon && (
          <i className="end-icon" style={{ width: "24px", height: "24px" }}>
            {endIcon}
          </i>
        )}
      </a>
      {!disableShadow && (
        <div className="dropium-btn-shadow" style={shadowStyle} />
      )}
    </div>
  );
};

export default DropiumButton;
