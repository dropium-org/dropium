import React from "react";
import { Route, Routes, useNavigate } from "react-router";
import "./profile-created-quests.css";
import DropiumButton from "components/dropium-button";

const ProfileCreatedQuests = () => {
  const navigate = useNavigate();
  return (
    <div className="create-quest-content-container">
      <div className="quest-main-content-filter">
        <div className="create-quest-container">
          <div>
          <DropiumButton
              activeEffectDisabled
              hoverEffectDisabled
              style={{
                padding: "20px 60px",
                width: "6em",
                letterSpacing: "1px",
                textTransform: "uppercase",
                fontFamily: "Lexend Zetta",
                fontStyle: "normal",
                fontWeight: "900",
                fontSize: "27px",
                lineHeight: "100%",
              }}
              borderSide={"left"}
            >
              QUESTS
            </DropiumButton>
          </div>
          <div className="create-quest-filter">
            <div className="create-quest-steps">
              <div className="create-quest-step">
                <DropiumButton
                  onClick={() => {}}
                  hoverEffectDisabled
                  shadowStyle={{ backgroundColor: "black" }}
                  style={{
                    padding: ".75em 2.5em",
                    width: "6em",
                    letterSpacing: "1px",
                    // textTransform: "uppercase",
                    fontStyle: "normal",
                    fontWeight: "500",
                    fontSize: "16px",
                    lineHeight: "100%",
                  }}
                >
                  On Going
                </DropiumButton>
              </div>
              <div className="create-quest-step">
                <DropiumButton
                  onClick={() => {}}
                  hoverEffectDisabled
                  shadowStyle={{ backgroundColor: "black" }}
                  style={{
                    padding: ".75em 2.5em",
                    width: "6em",
                    letterSpacing: "1px",
                    // textTransform: "uppercase",
                    fontStyle: "normal",
                    fontWeight: "500",
                    fontSize: "16px",
                    lineHeight: "100%",
                  }}
                >
                  Scheduled
                </DropiumButton>
              </div>
              <div className="create-quest-step">
                <DropiumButton
                  onClick={() => {}}
                  hoverEffectDisabled
                  shadowStyle={{ backgroundColor: "black" }}
                  style={{
                    padding: ".75em 2.5em",
                    width: "6em",
                    letterSpacing: "1px",
                    // textTransform: "uppercase",
                    fontStyle: "normal",
                    fontWeight: "500",
                    fontSize: "16px",
                    lineHeight: "100%",
                  }}
                >
                  Draft
                </DropiumButton>
              </div>
              <div className="create-quest-step">
                <DropiumButton
                  onClick={() => {}}
                  hoverEffectDisabled
                  shadowStyle={{ backgroundColor: "black" }}
                  style={{
                    padding: ".75em 2.5em",
                    width: "6em",
                    letterSpacing: "1px",
                    // textTransform: "uppercase",
                    fontStyle: "normal",
                    fontWeight: "500",
                    fontSize: "16px",
                    lineHeight: "100%",
                  }}
                >
                  Completed
                </DropiumButton>
              </div>
            </div>
            <div>
              <DropiumButton
                onButtonClicked={(e) => {
                  e.preventDefault();
                  navigate(`/app/profile/my-quests/create`);
                }}
                hoverEffectDisabled
                shadowStyle={{ backgroundColor: "#60ffe2" }}
                style={{
                  padding: ".75em 2.5em",
                  width: "12em",
                  letterSpacing: "1px",
                  // textTransform: "uppercase",
                  fontStyle: "normal",
                  fontWeight: "500",
                  fontSize: "16px",
                  lineHeight: "100%",
                }}
              >
                Create Quest
              </DropiumButton>
            </div>
          </div>
        </div>
      </div>
      <div className="quest-list-section">
        <div className="quests-categories">
          <div>Name</div>
          <div>Dropper</div>
          <div>Rewards</div>
          <div>Timeline</div>
        </div>
        <div className="quests-list"></div>
      </div>
    </div>
  );
};

export default ProfileCreatedQuests;
