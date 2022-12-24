import React, { useState } from "react";
import { useNavigate } from "react-router";
import "./create-quest-entries.css";
import { FiTwitter } from "react-icons/fi";
import { RxDiscordLogo } from "react-icons/rx";
import { TbBrandTelegram } from "react-icons/tb";

const CreateQuestEntries = ({
  setupTasks,
  setSetupTasks,
  taskIndex,
  setTaskIndex,
}) => {
  // const [setupTasks, setSetupTasks] = useState([])
  // const [taskIndex, setTaskIndex] = useState(0)
  const [taskInputLink, setTaskInputLink] = useState();

  const addTaskFollowTwitter = () => {
    setTaskIndex(taskIndex + 1);
    setSetupTasks((tasks) => [
      ...tasks,
      {
        taskName: "Follow On Twitter",
        id: `${taskIndex + 1}`,
      },
    ]);
  };
  const addTaskLikeTweet = () => {
    setTaskIndex(taskIndex + 1);
    setSetupTasks((tasks) => [
      ...tasks,
      {
        taskName: "Like This Tweet",
        id: `${taskIndex + 1}`,
      },
    ]);
  };
  const addTaskRetweet = () => {
    setTaskIndex(taskIndex + 1);
    setSetupTasks((tasks) => [
      ...tasks,
      {
        taskName: "Retweet This Tweet",
        id: `${taskIndex + 1}`,
      },
    ]);
  };
  const addTaskJoinDiscord = () => {
    setTaskIndex(taskIndex + 1);
    setSetupTasks((tasks) => [
      ...tasks,
      {
        taskName: "Join Discord Server",
        id: `${taskIndex + 1}`,
      },
    ]);
  };

  const handleRemoveTasks = (e) => {
    const id = e.target.id;
    const newTasksArray = setupTasks.filter((task) => task.id != id);
    setSetupTasks(newTasksArray);
  };


  //cần handle chỗ này 
  const handleAddTaskLink = (e) => {
    const id = e.target.id;
    const newTaskLink = setupTasks.filter((task) => task.id == id);
    // const taskLinkDict = newTaskLink[id];
    newTaskLink.map((taskLinkDict) => {
      setTaskInputLink(e.target.value);
      taskLinkDict.taskLink = taskInputLink;
      console.log(taskLinkDict);
      setSetupTasks((tasks) => [...tasks, taskLinkDict]);
    });
  };
  console.log(setupTasks);

  const renderTasks = (setupTasks) => {
    return setupTasks.map((task) => (
      <div className="style-quest-tasks-choose" key={task.id}>
        <div className="style-button-tasks-default-chosen">
          {task.taskName.includes("Discord") ? (
            <RxDiscordLogo />
          ) : (
            <FiTwitter />
          )}
          <span className="slyte-title-social-task">{task.taskName}</span>
          <a
            className="style-button-tasks-delete"
            id={task.id}
            onClick={handleRemoveTasks}
          >
            X
          </a>
        </div>
        <div className="profile-link-input">
          <div>Input your link</div>
          <div className="link-input-holder">
            <input
              className="link-input-box"
              placeholder="Your link"
              required
              id={task.id}
              onChange={handleAddTaskLink}
            ></input>
          </div>
        </div>
      </div>
    ));
  };
  return (
    <div>
      <div className="quest-section">
        <div>
          <div className="quest-title-box" id="quest-title">
            <div className="quest-title-box-style">
              <div className="quest-title-title">Choose a template</div>
            </div>
            <div className="quest-entries-input">
              <div className="quest-template-button-type-social">
                <div className="style-quest-button-social">
                  <a className="style-button-type-social">
                    <FiTwitter />
                    <span>Twitter</span>
                  </a>
                </div>
                <div className="style-quest-button-social">
                  <a className="style-button-type-social">
                    <RxDiscordLogo />
                    <span>Discord</span>
                  </a>
                </div>
                <div className="style-quest-button-social">
                  <a className="style-button-type-social">
                    <TbBrandTelegram />
                    <span>Telegram</span>
                  </a>
                </div>
                <div className="style-quest-button-social">
                  <a className="style-button-type-social">
                    {/* <img src={logoCircle} alt="" /> */}
                    <span>Website</span>
                  </a>
                </div>
              </div>
              <div className="quest-tasks-container">
                <div className="quest-task-default">
                  <div className="style-quest-tasks-social-default">
                    <a
                      className="style-button-tasks-default"
                      onClick={addTaskFollowTwitter}
                    >
                      <FiTwitter />
                      <span className="slyte-title-social-task">
                        Follow On Twitter
                      </span>
                    </a>
                  </div>
                  <div className="style-quest-tasks-social-default">
                    <a
                      className="style-button-tasks-default"
                      onClick={addTaskRetweet}
                    >
                      <FiTwitter />
                      <span className="slyte-title-social-task">
                        Retweet a Tweet
                      </span>
                    </a>
                  </div>
                  <div className="style-quest-tasks-social-default">
                    <a
                      className="style-button-tasks-default"
                      onClick={addTaskLikeTweet}
                    >
                      <FiTwitter />
                      <span className="slyte-title-social-task">
                        Like a Tweet
                      </span>
                    </a>
                  </div>
                  <div className="style-quest-tasks-social-default">
                    <a
                      className="style-button-tasks-default"
                      onClick={addTaskJoinDiscord}
                    >
                      <RxDiscordLogo />
                      <span className="slyte-title-social-task">
                        Join Discord Server
                      </span>
                    </a>
                  </div>
                </div>

                <div className="quest-tasks-choose">
                  {setupTasks && renderTasks(setupTasks)}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div className="button-save-container"></div>
    </div>
  );
};

export default CreateQuestEntries;
