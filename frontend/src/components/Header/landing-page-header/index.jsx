import DropiumButton from "components/dropium-button";
import React from "react";
import { useNavigate } from "react-router-dom";
import Header from "../header";

const LandingPageHeader = () => {

  return <Header style= {{width: "calc(100% - 50%)"}}/>;

  const navigate = useNavigate();
  return (
    <Header
      style={{ width: "calc(100% - 36%)" }}
      buttonBox={<DropiumButton borderSide={"left"}>Launch App</DropiumButton>}
      onClick={() => {
        navigate(`/app`);
      }}
    />
  );

};

export default LandingPageHeader;
