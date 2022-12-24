import React, { useContext, useState } from "react";
import { QuestContext } from "../../../contexts/quest-context";
import { Space, DatePicker } from "antd";
import "./create-quest-setup.css";
import dayjs from "dayjs";

const CreateQuestSetup = ({
  questTitle,
  questDescription,
  setQuestTitle,
  setQuestDescription,
  startDate,
  setStartDate,
  endDate,
  setEndDate
}) => {
  const { quest, setQuest } = useContext(QuestContext);
  const dateFormat = "DD/MM/YYYY";

  const handleTitleChange = (e) => {
    setQuestTitle(e.target.value);
  };

  const handleDescriptionChange = (e) => {
    setQuestDescription(e.target.value);
  };

  const handleStartDateChange = (value) => {
    setStartDate(dayjs(value).format());
  };

  const handleEndDateChange = (value) => {
    setEndDate(dayjs(value).format());
  };
  return (
    <>
      <div className="quest-section">
        <div className="quest-title-box" id="quest-title">
          <div className="quest-title-box-style">
            <div className="quest-title-title">Quest Title</div>
          </div>
          <div className="quest-title-input">
            <textarea
              className="textarea-quest-title"
              cols="30"
              rows="10"
              required
              onChange={handleTitleChange}
              value={questTitle}
            ></textarea>
          </div>
        </div>
        <div>
          <div className="quest-title-box" id="quest-title">
            <div className="quest-title-box-style">
              <div className="quest-title-title">Description</div>
            </div>
            <div className="quest-input">
              <textarea
                className="textarea-description"
                cols="30"
                rows="10"
                required
                onChange={handleDescriptionChange}
                value={questDescription}
              ></textarea>
            </div>
          </div>
        </div>
        <div>
          <div className="quest-title-box" id="quest-title">
            <div className="quest-title-box-style">
              <div className="quest-title-title">Schedule</div>
            </div>
            <div className="quest-input">
              <div className="quest-schedule-date">
                <div className="quest-schedule-select-table">
                  <div>
                    <span>Starts</span>
                  </div>
                  <div className="style-container-calender">
                    <Space direction="vertical" size={15}>
                      <DatePicker
                        style={{
                          border: "4px solid black",
                        }}
                        onChange={handleStartDateChange}
                        format={dateFormat}
                      />
                    </Space>
                  </div>
                </div>
                <div className="quest-schedule-select-table">
                  <div>
                    <span>Ends</span>
                  </div>
                  <div className="style-container-calender">
                    <Space direction="vertical" size={15}>
                      <DatePicker
                        style={{
                          border: "4px solid black",
                        }}
                        onChange={handleEndDateChange}
                        format={dateFormat}
                      />
                    </Space>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default CreateQuestSetup;
