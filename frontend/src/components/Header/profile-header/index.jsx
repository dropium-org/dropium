import React from "react";
import Header from "../header";
import ProfileHeaderMenu from "./profile-header-menu";
import ProfileHeaderButtonBox from "./profile-header-button-box";

const ProfileHeader = () => {
  return <Header menu={<ProfileHeaderMenu />} buttonBox={<ProfileHeaderButtonBox/>} />;
};

export default ProfileHeader;
