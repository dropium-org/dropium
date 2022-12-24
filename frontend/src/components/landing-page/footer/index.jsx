import React from "react";
import dropLogo from "assets/landing-page/icons/drop.png";
import disLogo from "assets/landing-page/icons/Mask group-1.png";
import teleLogo from "assets/landing-page/icons/Mask group-2.png";
import twLogo from "assets/landing-page/icons/Mask group.png";
import worldLogo from "assets/landing-page/icons/world.png";
import "./landing-footer.css";
const LandingPageFooter = () => {
  return (
    <div className="footer-wrapper">
      <div className="footer-content">
        <div className="footer-title-wrapper">
          {/* 1 */}
          <div className="footer-title">
            <img src={dropLogo} alt="drop-logo" className="logo-dropium" />
            <span className="title-dropium">DROPIUM</span>
          </div>

          <span className="title-real">
             An all for community platform with
            <br />
            “REAL" solutions
          </span>

          <div className="button-wrapper">
            <button className="button-email">Your Email</button>
            <button className="button-signup">Sign Up</button>
          </div>

          <div className="img-list-wrapper">
            <img src={twLogo} alt="tw-logo" className="twitter-logo" />
            <img
              src={disLogo}
              alt="dis-logo"
              className="discord-logo"
              href="1"
            />
            <img
              src={teleLogo}
              alt="tele-logo"
              className="tele-logo"
              href="2"
            />
            <img
              src={worldLogo}
              alt="world-logo"
              className="world-logo"
              href="3"
            />
          </div>
        </div>

        <div className="footer-about-wrapper">
          <span className="title-about">About Us</span>
          <span className="title-comms">Discover <br/>Communities</span>
        </div>
      </div>
    </div>
  );
};
export default LandingPageFooter;
