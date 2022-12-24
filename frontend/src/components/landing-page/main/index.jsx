import React from "react";
import "./landing-body.css";
import frame from "./Cover.png";
import DropiumButton from "components/dropium-button";
const LandingBody = () => {
  return (
    <div className="body-wrapper">
      <div className="body-content-wrapper">

        <div className="body-frame-img-wrapper">
          <img src={frame} className="frame-img"></img>
        </div>

        <div className="body-title-wrapper">
          <div className="title-body">A Decentralized Growth Bootstrapping Platform for fairness, transparency and time-savings</div>
      
          <div className="body-button-wrapper">
              <DropiumButton
              borderSide={"left"}
              >
                Explore
              </DropiumButton>
              <DropiumButton
              borderSide={"left"}
              // hoverEffectDisabled
              >
                Create Comunity
              </DropiumButton>
          </div>

        </div>          
      </div>
    </div>
  );
};
export default LandingBody;
