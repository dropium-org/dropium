import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { BsGift } from "react-icons/bs";
import { FiSettings } from "react-icons/fi";
import "./profile-sidebar.css";
import img_community from "../../assets/sidebar/logo_community_test.svg";
import logo_circle from "../../assets/sidebar/circle-logo.svg";

const ProfileSidebar = () => {
  const navigate = useNavigate();
  useEffect(() => {
    const menuSidebarBtn = document.querySelectorAll(
      ".sidebar-quest-section button"
    );
    menuSidebarBtn.forEach((btn) => {
      btn.addEventListener("click", (e) => {
        document
          .querySelector(".sidebar-quest-section button.active")
          .classList.remove("active");
        e.target.classList.add("active");
      });
    });
  });

  return (
    <div className="quest-sidebar">
      <div className="style-sidebard-community">
        <div className="style-logoBox-community">
          <div className="style-logo-community" id="sidebar">
            <div className="style-imgbox-community">
              <img src={img_community} alt="" width="50px" heigh="50px" />
            </div>
          </div>
          <div className="style-community-card">
            <span>Yeeha Games</span>
          </div>
        </div>
      </div>
      <div className="sidebar-quests-section">
        <div className="sidebar-quest-section">
          <button
            className="active"
            onClick={() => {
              navigate("/app/profile/my-quests");
            }}
          >
            My Quests
            <div>
              <img src={logo_circle} alt="" width="16px" height="16px" />
            </div>
          </button>
          <button
            onClick={() => {
              navigate("/app/profile");
            }}
          >
            Reward History
            <div>
              <BsGift />
            </div>
          </button>
          <button
            onClick={() => {
              navigate("/app/profile");
            }}
          >
            Community Settings
            <div>
              <FiSettings />
            </div>
          </button>
        </div>
      </div>
      <div className="sidebar-footer">
        <div className="style-sidebar-footer">More</div>
        <div className="style-sidebar-footer">...</div>
      </div>
    </div>
  );
};

export default ProfileSidebar;
