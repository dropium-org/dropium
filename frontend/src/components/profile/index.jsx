import React from "react";
import { Outlet } from "react-router-dom";
import ProfileSidebar from "../profile-sidebar";
import "./profile.css";

const Profile = () => {
  return (
    <div className="profile-container">
      <ProfileSidebar/>
      <Outlet/>
    </div>
  );
};

export default Profile;
