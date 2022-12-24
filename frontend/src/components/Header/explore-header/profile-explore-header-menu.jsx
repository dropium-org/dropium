import React, { useEffect } from "react";
import "./profile-explore-header-menu.css";

export default function ProfileHeaderExploreMenu() {
  useEffect(() => {
    const menuHeaderExploreBtt = document.querySelectorAll(
      ".style-header-menu-explore button"
    );
    menuHeaderExploreBtt.forEach((btn) => {
      btn.addEventListener("click", (e) => {
        console.log("da click");
        document
          .querySelector(".style-header-menu-explore button.active")
          .classList.remove("active");
        e.target.classList.add("active");
      });
    });
  }, []);

  return (
    <div className="style-header-menu-explore">
      <button className="active">Home</button>
      <button>Explore</button>
      <button>Communities</button>
    </div>
  );
}
