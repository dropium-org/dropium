import React from "react";
import Header from "../header";
import ProfileHeaderButtonBox from "../profile-header/profile-header-button-box";
import ProfileHeaderExploreMenu from "./profile-explore-header-menu";

const ExploreHeader = () => {
  return (
    <Header
      menu={<ProfileHeaderExploreMenu />}
      buttonBox={<ProfileHeaderButtonBox />}
    />
  );
};

export default ExploreHeader;
