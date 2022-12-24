import React, { useState } from "react";
import "./create-quest.css";
import CreateQuestEntries from "./create-quest-entries";
import CreateQuestReward from "./create-quest-reward";
import DropiumButton from "../dropium-button";
import CreateQuestSetup from "./create-quest-setup";
import { QuestContextProvider } from "../../contexts/quest-context";
import * as buffer from "buffer";
import { useConnection, useWallet } from "@solana/wallet-adapter-react";
import { AiOutlineLoading3Quarters } from "react-icons/ai";
import {
  LAMPORTS_PER_SOL,
  PublicKey,
  SystemProgram,
  Transaction,
} from "@solana/web3.js";
import { createQuestAsync } from "apis/dropium-api";

const CreateQuestPage = () => {
  const { connection } = useConnection();
  const { publicKey, sendTransaction } = useWallet();
  const [currentStepIndex, setCurrentStepIndex] = useState(0);
  const onStepChange = (stepIndex) => {
    setCurrentStepIndex(stepIndex);
  };
  const [questTitle, setQuestTitle] = useState();
  const [questDescription, setQuestDescription] = useState();
  const [startDate, setStartDate] = useState();
  const [endDate, setEndDate] = useState();
  const [rewardSlots, setRewardSlots] = useState();
  const [rewardType, setRewardType] = useState(0);
  const [tasksSelected, setTasksSelected] = useState([]);
  const [setupTasks, setSetupTasks] = useState([]);
  const [taskIndex, setTaskIndex] = useState(0);

  const data = {
    communityId: 1,
    description: `${questDescription}`,
    eligibility: "0",
    endAt: `${endDate}`,
    logo: "",
    network: "mainnet-beta",
    rewardSlots: `${rewardSlots}`,
    rewardType: `${rewardType}`,
    startAt: `${startDate}`,
    status: "0",
    title: `${questTitle}`,
    tasks: [
      {
        extra: {},
        type: "0",
      },
      {
        extra: {},
        type: "0",
      },
    ],
  };

  window.Buffer = buffer.Buffer;
  const onRewardInfoClicked = (e) => {
    e.preventDefault();
  };

  const sendTransction = async () => {
    const to = PublicKey.unique();
    const transaction = new Transaction().add(
      SystemProgram.transfer({
        fromPubkey: publicKey,
        toPubkey: to,
        lamports: 0.1 * LAMPORTS_PER_SOL,
      })
    );

    // Sign transaction, broadcast, and confirm
    const signature = await sendTransaction(transaction, connection, [
      publicKey,
    ]);

    return signature;
  };

  const createQuest = async (e) => {
    e.preventDefault();
    try {
      let questCreateRequest = await createQuestAsync(data);
    } catch (err) {
      console.log(err);
    }
  };

  const createQuestStepsNavigatorItem = (stepIndex, stepName) => (
    <div key={stepName} className="create-quest-step">
      <div>{stepIndex + 1}</div>
      <div>
        <DropiumButton
          onButtonClicked={() => {
            onStepChange(stepIndex);
          }}
          hoverEffectDisabled
          style={{
            padding: ".75em 2.5em",
            width: "2em",
            letterSpacing: "1px",
            textTransform: "uppercase",
            fontStyle: "normal",
            fontWeight: "500",
            fontSize: "16px",
            lineHeight: "100%",
          }}
        >
          {stepName}
        </DropiumButton>
      </div>
    </div>
  );

  const steps = ["Set up", "Entries", "Reward"];

  const createQuestStepsNavigator = () => (
    <nav className="create-quest-steps">
      {steps.map((value, index) => createQuestStepsNavigatorItem(index, value))}
    </nav>
  );

  const renderCurrentStep = (stepIndex) => {
    switch (stepIndex) {
      case 0:
        return (
          <>
            <CreateQuestSetup
              questTitle={questTitle}
              questDescription={questDescription}
              setQuestTitle={setQuestTitle}
              setQuestDescription={setQuestDescription}
              startDate={startDate}
              setStartDate={setStartDate}
              endDate={endDate}
              setEndDate={setEndDate}
            />
          </>
        );
      case 1:
        return (
          <>
            <CreateQuestEntries
              setupTasks={setupTasks}
              setSetupTasks={setSetupTasks}
              taskIndex={taskIndex}
              setTaskIndex={setTaskIndex}
            />
          </>
        );
      case 2:
        return (
          <>
            <CreateQuestReward
              rewardSlots={rewardSlots}
              setRewardSlots={setRewardSlots}
              rewardType={rewardType}
              setRewardType={setRewardType}
            />
          </>
        );
      default:
        return <>Invalid step index</>;
    }
  };

  return (
    <div className="create-quest-content-container">
      <div className="quest-main-content">
        <div className="create-quest-container">
          <div>
            <DropiumButton
              activeEffectDisabled
              hoverEffectDisabled
              style={{
                padding: "20px 60px",
                width: "12em",
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
              CREATE A QUEST
            </DropiumButton>
          </div>
          {createQuestStepsNavigator()}
        </div>
      </div>
      <QuestContextProvider>
        <div className="quest-section">
          {renderCurrentStep(currentStepIndex)}
        </div>
        <div className="button-save-container">
          <DropiumButton
            onButtonClicked={async (e) => {
              e.preventDefault();
              //save quest data
              // TODO
              if (currentStepIndex < steps.length - 1) {
                //move to next step
                setCurrentStepIndex((cur) => cur + 1);
              } else {
                //submit
                // TODO
                await sendTransction();
                await createQuest(e);
              }
            }}
            hoverEffectDisabled
            shadowStyle={{ backgroundColor: "#60ffe2" }}
            style={{
              padding: ".75em 2.5em",
              width: "2em",
              letterSpacing: "1px",
              textTransform: "uppercase",
              fontStyle: "normal",
              fontWeight: "500",
              fontSize: "16px",
              lineHeight: "100%",
            }}
          >
            {currentStepIndex < steps.length - 1 ? "Next" : "Submit"}
          </DropiumButton>
        </div>
      </QuestContextProvider>
    </div>
  );
};

export default CreateQuestPage;
