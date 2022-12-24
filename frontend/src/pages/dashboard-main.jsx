import React from "react";
import { Outlet } from "react-router-dom";
import "./dashboard-main.css"
function DashboardMain() {
  return (
    <>
      <main className="main-content-display-container" style={{ height: "120vh" }}>
        <Outlet />
      </main>
    </>
  );
}

export default DashboardMain;
