import React, { useState } from "react";
import "./reward-panel.css";
import topShadow from "assets/dropium-panel/top-panel-shadow.png";
import topPanel from "assets/dropium-panel/top-panel.png";
import botShadow from "assets/dropium-panel/bot-panel-shadow.png";
import botPanel from "assets/dropium-panel/bot-panel.png";
import * as buffer from "buffer";
import { useConnection, useWallet } from "@solana/wallet-adapter-react";
import { AiOutlineLoading3Quarters } from "react-icons/ai";
import {
  LAMPORTS_PER_SOL,
  PublicKey,
  SystemProgram,
  Transaction,
} from "@solana/web3.js";
const RewardPanel = () => {
  const { connection } = useConnection();
  const { publicKey, sendTransaction } = useWallet();
  const [btnName, setBtnName] = useState("Submit");
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
  const onRewardClaimeClicked = async (e) => {
    e.preventDefault();

    if (btnName === "Submit") {
      setBtnName(
        <i className="loading">
          <AiOutlineLoading3Quarters />
        </i>
      );
      try {
        const hash = await sendTransction();
      } finally {
        setBtnName("Claim");
      }
    } else {
      setBtnName(
        <i className="loading">
          <AiOutlineLoading3Quarters />
        </i>
      );
      try {
        const hash = await sendTransction();
      } finally {
        setBtnName("Claimed");
      }
    }
  };

  return (
    <div class="quest-detail-reward-panel">
      <div className="reward-info">
        <a href="/#" onClick={onRewardInfoClicked} className="reward-btn ">
          <img src={topPanel} width={"100%"} alt="top-panel" />
          <div>
            <div className="reward-info-title">
              <span>Reward</span>
            </div>
            <div className="reward-info-detail">
              <span>1000$</span>
            </div>
          </div>
        </a>
        <img src={topShadow} width={"100%"} alt="top-panel-shadow" />
      </div>
      <div className={`reward-claim-button`}>
        <a
          href="/#"
          onClick={onRewardClaimeClicked}
          className={`reward-btn activable ${
            btnName === "Claimed" ? "active" : ""
          }`}
        >
          <img src={botPanel} width={"100%"} alt="bot-panel" />
          <div>
            <div className="reward-claim-inner">
              <span>{btnName}</span>
            </div>
          </div>
        </a>
        <img src={botShadow} width={"100%"} alt="bot-panel-shadow" />
      </div>
    </div>
  );
};

export default RewardPanel;
