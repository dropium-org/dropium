import DropiumButton from "components/dropium-button";
import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import "./quest-detail.css";
import { SlSocialTwitter } from "react-icons/sl";
import { RxDiscordLogo } from "react-icons/rx";
import DropiumPanel from "components/dropium-panel";
import RewardPanel from "components/quest-detail-reward-panel";
import logo from "assets/quest-detail/logo.png";
const QuestDetail = (props) => {
  const params = useParams();
  const { questId } = params;
  const [questInfo, setQuestInfo] = useState(null);
  useEffect(() => {
    // id=27
    setQuestInfo({
      communityId: 13892774,
      description:
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum",
      eligibility: "0",
      endAt: "2022/12/26 20:00",
      id: -86715491,
      logo: logo,
      network: "mainnet-beta",
      rewardSlots: -51513266,
      rewardType: "0",
      startAt: "2022/12/03 20:00",
      status: "0",
      title: "MERRY XMAS EVENT",
      tasks: [
        {
          extra: {
            userTag: "solana",
          },
          id: -41815141,
          type: TaskType.TWITTER_FOLLOW,
        },
        {
          extra: {
            tweetId: "1602428624375877635",
          },
          id: -54145602,
          type: TaskType.TWITTER_SHARE_POST,
        },
        {
          extra: {
            tweetId: "1602428624375877635",
          },
          id: -54145602,
          type: TaskType.TWITTER_LIKE_POST,
        },
        {
          extra: {
            inviteUrl: "https://discord.gg/EFmZAAtg",
            inviteCode: "EFmZAAtg",
          },
          id: -54145602,
          type: TaskType.DISCORD_JOIN_SERVER,
        },
      ],
    });
  },[]);

  const TaskType = {
    DISCORD_JOIN_SERVER: "0",

    TWITTER_LIKE_POST: "10",
    TWITTER_SHARE_POST: "11",
    TWITTER_FOLLOW: "12",
  };

  const loadTaskIconByTaskType = (taskType) => {
    switch (taskType) {
      case TaskType.TWITTER_FOLLOW:
      case TaskType.TWITTER_SHARE_POST:
      case TaskType.TWITTER_LIKE_POST:
        return <SlSocialTwitter size={24} />;
      case TaskType.DISCORD_JOIN_SERVER:
        return <RxDiscordLogo size={24} />;

      default:
        return null;
    }
  };

  const loadTaskTitleByTaskType = (taskType) => {
    switch (taskType) {
      case TaskType.TWITTER_FOLLOW:
        return "Follow Twitter";
      case TaskType.TWITTER_SHARE_POST:
        return "Share a tweet";
      case TaskType.TWITTER_LIKE_POST:
        return "Share a tweet";
      case TaskType.DISCORD_JOIN_SERVER:
        return "Join Discord server";

      default:
        return null;
    }
  };

  const loadTaskActionByTaskType = (taskType) => {
    switch (taskType) {
      case TaskType.TWITTER_FOLLOW:
        return "Follow";
      case TaskType.TWITTER_SHARE_POST:
        return "Share";
      case TaskType.TWITTER_LIKE_POST:
        return "Like";
      case TaskType.DISCORD_JOIN_SERVER:
        return "Join server";

      default:
        return null;
    }
  };

  const handleOpenBrowser = (url, urlRegex, width = 550, height = 420) => {
    if (urlRegex ? url.match(urlRegex) : false) return;
    const winWidth = window.screen.width;
    const winHeight = window.screen.height;
    let left = Math.round(winWidth / 2 - width / 2);
    let top = 0;
    // "toolbar=0,status=0,width=548,height=325"
    const windowOptions =
      "scrollbars=yes,resizable=yes,toolbar=no,location=yes";
    if (winWidth > height) {
      top = Math.round(winHeight / 2 - height / 2);
    }

    window.open(
      url,
      "intent",
      windowOptions +
        ",width=" +
        width +
        ",height=" +
        height +
        ",left=" +
        left +
        ",top=" +
        top
    );
  };

  const doTaskByTaskType = {};
  doTaskByTaskType[TaskType.DISCORD_JOIN_SERVER] = (task) => {
    const extra = task?.extra;
    handleOpenBrowser(
      extra?.inviteUrl || `https://discord.gg/${extra?.inviteCode}`
    );
  };
  doTaskByTaskType[TaskType.TWITTER_LIKE_POST] = (task) => {
    const extra = task?.extra;
    handleOpenBrowser(
      `https://twitter.com/intent/like?tweet_id=${extra.tweetId}`
    );
  };
  doTaskByTaskType[TaskType.TWITTER_FOLLOW] = (task) => {
    const extra = task?.extra;
    handleOpenBrowser(
      `https://twitter.com/intent/follow?screen_name=${extra.userTag}`
    );
  };
  doTaskByTaskType[TaskType.TWITTER_SHARE_POST] = (task) => {
    const extra = task?.extra;
    handleOpenBrowser(
      `https://twitter.com/intent/retweet?tweet_id=${extra.tweetId}`
    );
  };

  const onDoTaskButtonClicked = (task, event) => {
    doTaskByTaskType[task?.type]?.(task);
  };

  return (
    <div className="quest-detail-wrapper">
      <div className="quest-detail">
        <div className="banner">
          <div className="banner-left">
            <div className="banner-heading">
              <div>
                <DropiumButton
                  hoverEffectDisabled
                  borderSide={"left"}
                  style={{
                    height: "2em",
                    width: "3em",
                    fontSize: "16px",
                    fontWeight: "500",
                    padding: "20px 50px",
                  }}
                >
                  Share on <br /> Twitter
                </DropiumButton>
              </div>
              <div>
                <h2>DROPIUM</h2>
                <h1>{questInfo?.title}</h1>
              </div>
            </div>
            <div className="banner-info">
              <DropiumButton
                hoverEffectDisabled
                activeEffectDisabled
                borderSide={"both"}
                style={{
                  //   height: "2em",
                  //   width: "3em",
                  fontSize: "16px",
                  fontWeight: "500",
                  //   padding: "20px 50px",
                }}
                disableShadow
              >
                {questInfo?.status == 0 ? "On going" : "..."}
              </DropiumButton>
              <DropiumButton
                hoverEffectDisabled
                activeEffectDisabled
                borderSide={"both"}
                style={{
                  fontSize: "16px",
                  width: "30em",
                  fontWeight: "500",
                }}
                disableShadow
              >
                {questInfo?.startAt}~{questInfo?.endAt}
              </DropiumButton>
            </div>
          </div>
          <div className="banner-right">
            <div className="banner-logo">
              <img src={questInfo?.logo} height={"100%"} alt="banner-logo" />
            </div>
          </div>
        </div>
        <div className="tasks-panel">
          <div className="tasks-list-wrapper">
            <ul>
              {questInfo?.tasks?.map((task) => (
                <>
                  <li>
                    <DropiumPanel
                      startIcon={loadTaskIconByTaskType(task?.type)}
                      title={loadTaskTitleByTaskType(task?.type)}
                      contentStyle={{
                        display: "flex",
                        justifyContent: "space-evenly",
                      }}
                      style={{
                        width: "95%",
                      }}
                    >
                      <DropiumButton
                        hoverEffectDisabled
                        style={{ backgroundColor: "white", color: "black" }}
                        onButtonClicked={(e) => onDoTaskButtonClicked(task, e)}
                      >
                        {loadTaskActionByTaskType(task?.type)}
                      </DropiumButton>
                      {/* <DropiumButton
                        hoverEffectDisabled
                        style={{ backgroundColor: "white", color: "black" }}
                      >
                        Verify
                      </DropiumButton> */}
                    </DropiumPanel>
                  </li>
                </>
              ))}
            </ul>
            <div className="quest-description">
              <h2>DESCRIPTION</h2>
              <p>{questInfo?.description}</p>
            </div>
          </div>
          <div className="reward-panel">
            <RewardPanel />
          </div>
        </div>
      </div>
    </div>
  );
};

export default QuestDetail;
