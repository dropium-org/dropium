import React from "react";
import DropiumButton from "../../dropium-button";

const ProfileHeaderMenu = () => {
  return (
    <div className="profile-header-menu">
      <DropiumButton
        borderSide={"left"}
        style={{
          zIndex: 3,
        }}
      >
        Profile
      </DropiumButton>
      <DropiumButton
        borderSide={"right"}
        style={{
          backgroundColor: "white",
          color: "black",
          zIndex: 4,
        }}
      >
        Community
      </DropiumButton>
    </div>
  );
};

export default ProfileHeaderMenu;
