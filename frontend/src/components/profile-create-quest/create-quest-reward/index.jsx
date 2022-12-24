import React, { useContext, useState } from "react";
import { createQuestAsync } from "../../../apis/dropium-api";
import DropiumButton from "../../dropium-button";
import "./create-quest-reward.css";
import { Input, Select, InputNumber } from "antd";
import logo_solana from "../../../assets/create-quest/logo-solana.svg";

const CreateQuestReward = ({ rewardSlots, setRewardSlots, rewardType, setRewardType }) => {
  const createQuest = async (e) => {
    e.preventDefault();
    try {
      let questCreateRequest = await createQuestAsync();
    } catch (err) {
      console.log(err);
    }
  };
  const { Option } = Select;

  const handleRewardSlots = (e) => {
    setRewardSlots(e.target.value);
  };

  const handleRewardFcfs = (e) => {
    setRewardType(0)
  }

  const handleRewardLuckyDraw = (e) => {
    setRewardType(1)
  }
  console.log(rewardType)
  return (
    <div className="create-quest-content-reward-container">
      <div className="quest-section">
        <div className="style-create-quest-stt" id="quest-title">
          <div className="quest-title-box-style">
            <div className="quest-title-title">Reward Method</div>
          </div>
          <div className="quest-title-box-style-input">
            <div className="style-create-reward-method-btt">
              <DropiumButton
                onButtonClicked={handleRewardFcfs}
                hoverEffectDisabled
                shadowStyle={{ backgroundColor: "#60ffe2" }}
                style={{
                  padding: ".75em 2.5em",
                  width: "12em",
                  letterSpacing: "1px",
                  fontStyle: "normal",
                  fontWeight: "500",
                  fontSize: "16px",
                  lineHeight: "100%",
                }}
              >
                First Come First Served
              </DropiumButton>
            </div>
            <div className="style-create-reward-method-btt lucky-draws">
              <DropiumButton
                onButtonClicked={handleRewardLuckyDraw}
                hoverEffectDisabled
                shadowStyle={{ backgroundColor: "#60ffe2" }}
                style={{
                  padding: ".75em 2.5em",
                  width: "5em",
                  letterSpacing: "1px",
                  // textTransform: "uppercase",
                  fontStyle: "normal",
                  fontWeight: "500",
                  fontSize: "16px",
                  lineHeight: "100%",
                  // cursor: "not-allowed",
                }}
              >
                Lucky Draws
              </DropiumButton>
            </div>
          </div>
        </div>
        <div className="style-create-quest-stt" id="quest-title">
          <div className="quest-title-box-style">
            <div className="quest-title-title">Network</div>
          </div>
          <div className="quest-title-box-network">
            <select id="" className="style-quest-network">
              <option value="Option 1">
                Solana
                {/* <span>Solana</span>
                <img src={logo_solana} alt="" /> */}
                {/* TODO Menu with icon */}
              </option>
              <option value="Option 2">Comming Soon</option>
              <option value="Option 3">Comming Soon</option>
              <option value="Option 4">Comming Soon</option>
            </select>
          </div>
        </div>
        <div className="style-create-quest-stt" id="quest-title">
          <div className="quest-title-box-style">
            <div className="quest-title-title">Number of Reward</div>
          </div>
          <div className="quest-title-box-number-reward">
            <div className="style-quest-number-reward">
              <input
                className="textarea-number-reward"
                cols="30"
                rows="10"
                typeof="number"
                onChange={handleRewardSlots}
                value={rewardSlots}
                required
                type="number"
              >
              </input>
            </div>
          </div>
        </div>
        <div className="style-create-quest-stt" id="quest-title">
          <div className="quest-title-box-style">
            <div className="quest-title-title">Reward</div>
          </div>
          <div className="quest-title-box-style-input">
            <div className="style-create-quest-reward-box">
              <div className="style-reward-box-whitelist">
                <span>Whitelist</span>
              </div>
              <div className="style-reward-box-token">
                <div className="style-reward-box-token-title">
                  <span>Token</span>
                </div>
                <div className="style-reward-box-token-detail">
                  <div className="style-reward-box-money-detail">
                    <Input.Group compact>
                      <Input
                        style={{ width: "50%", border: "4px solid black" }}
                        placeholder="Input Value"
                        type="number"
                        required
                      />
                      <Select
                        defaultValue="USDT"
                        style={{ border: "4px solid black" }}
                      >
                        <Option value="USDT">USDT</Option>
                        <Option value="BUSD">BUSD</Option>
                      </Select>
                    </Input.Group>
                  </div>
                  <div className="style-reward-box-token-person">
                    <InputNumber
                      min={1}
                      max={1000}
                      placeholder="Reward per person"
                      style={{ width: "100%", border: "4px solid black" }}
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CreateQuestReward;
