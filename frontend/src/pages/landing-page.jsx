import React from "react";
import LandingPageHeader from "../components/header/landing-page-header";
import LandingPageFooter from "../components/landing-page/footer";
import LandingBody from "../components/landing-page/main";

function LandingPage() {
  return (
    <>
      <LandingPageHeader />
      <LandingBody/>
      <LandingPageFooter/>
    </>
  );
}

export default LandingPage;
