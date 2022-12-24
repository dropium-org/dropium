import React, { useEffect } from "react";
import "./explore-main.css";
import dropiumLogo from "../../assets/quest-detail/logo.png";
import magicEden from "../../assets/explore/me.png";
import degods from "../../assets/explore/degods.png";
import DropiumButton from "components/dropium-button";
import RewardToken from "components/dropium-reward/reward-token";
import RewardNft from "components/dropium-reward/reward-nft";
import { createQuestAsync } from "apis/dropium-api";


export default function ExploreMain() {
  useEffect(() => {
    // //filter , button catagory
    // const categoryBtt = document.querySelectorAll(".button-category button");
    // const popularBoxList = document.querySelectorAll(".style-listItemBox");
    // categoryBtt.forEach((btn) => {
    //   btn.addEventListener("click", (e) => {
    //     console.log("click");
    //     const type = e.target.getAttribute("type-category");

    //     //remove and set active button
    //     document
    //       .querySelector(".button-category button.active")
    //       .classList.remove("active");
    //     e.target.classList.add("active");

    //     //filter element
    //     popularBoxList.forEach((item) => {
    //       if (type === "All" || item.getAttribute("type-category") === type)
    //         item.classList.remove("hide");
    //       else item.classList.add("hide");
    //     });
    //   });
    // });

    

  }, []);
  return (
    <div>
      <div className="style-page">
        <div className="style-container">
          <div className="style-content-quest">
            <div>
              <DropiumButton
                activeEffectDisabled
                hoverEffectDisabled
                style={{
                  padding: "20px 60px",
                  width: "5em",
                  letterSpacing: "1px",
                  textTransform: "uppercase",
                  fontFamily: "Lexend Zetta",
                  fontStyle: "normal",
                  fontWeight: "900",
                  fontSize: "27px",
                  lineHeight: "100%",
                }}
                borderSide={"left"}
              >
                QUEST
              </DropiumButton>
            </div>
          </div>
          {/* <div className="style-explore-category">
            <div className="button-category">
              <button className="active" type-category="All">
                All
              </button>
              <button type-category="NFT">NFT</button>
              <button type-category="DAO">DAO</button>
              <button type-category="GameFi">GameFi</button>
              <button type-category="Social">Social</button>
              <button type-category="Metaverse">Metaverse</button>
              <button type-category="Tool">Tool</button>
              <button type-category="Eco System">Eco System</button>
              <button type-category="Other">Other</button>
            </div>
          </div>
          <div className="style-explore-filter">
            <div className="style-explore-detail-filter">
              <DropiumButton
                onClick={() => {}}
                hoverEffectDisabled
                shadowStyle={{ backgroundColor: "black" }}
                style={{
                  padding: ".75em 2.5em",
                  width: "6em",
                  letterSpacing: "1px",
                  fontStyle: "normal",
                  fontWeight: "500",
                  fontSize: "16px",
                  lineHeight: "100%",
                }}
                borderSide="left"
              >
                Available
              </DropiumButton>
            </div>
            <div className="style-explore-detail-filter">
              <DropiumButton
                onClick={() => {}}
                hoverEffectDisabled
                shadowStyle={{ backgroundColor: "black" }}
                style={{
                  padding: ".75em 2.5em",
                  width: "6em",
                  letterSpacing: "1px",
                  fontStyle: "normal",
                  fontWeight: "500",
                  fontSize: "16px",
                  lineHeight: "100%",
                }}
                borderSide="none"
              >
                All Rewards
              </DropiumButton>
            </div>
            <div className="style-explore-detail-filter">
              <DropiumButton
                onClick={() => {}}
                hoverEffectDisabled
                shadowStyle={{ backgroundColor: "black" }}
                style={{
                  padding: ".75em 2.5em",
                  width: "6em",
                  letterSpacing: "1px",
                  fontStyle: "normal",
                  fontWeight: "500",
                  fontSize: "16px",
                  lineHeight: "100%",
                }}
                borderSide="right"
              >
                All Communities
              </DropiumButton>
            </div>
          </div> */}
          <div className="style-explore-itemBox">
            <div className="style-popularBox">
              <div className="style-listItemBox" type-category="NFT">
                <div className="style-itemBox" target="_blank">
                  <div className="style-container_itemBox">
                    <div className="style-display-itemBox">
                      <div className="style-information-itemBox">
                        <div className="style-content-card">
                          <div className="style-logoBox-card">
                            <div className="style-logo-card">
                              <div className="style-imgbox-card"></div>
                              <div className="style-icon-certify"></div>
                            </div>
                            <div className="style-community-card">
                              <span>Dropium</span>
                            </div>
                          </div>
                        </div>
                        <h3 className="style-title-content">
                          Welcome all new Users to Dropium
                        </h3>
                        <div className="style-rewardsBox-card">
                          <div className="style-container-rewards">
                            <div className="style-content-rewards">
                              <RewardToken typeToken="sol" valueToken="20000" />
                              <RewardNft />
                            </div>  
                          </div>
                        </div>
                      </div>
                      <div className="style-background-card">
                        <div className="style-img-community-circle-image">
                          <img src={dropiumLogo} alt="" />
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div className="style-listItemBox" type-category="GameFi">
                <div className="style-itemBox" target="_blank">
                  <div className="style-container_itemBox">
                    <div className="style-display-itemBox">
                      <div className="style-information-itemBox">
                        <div className="style-content-card">
                          <div className="style-logoBox-card">
                            <div className="style-logo-card">
                              <div className="style-imgbox-card"></div>
                              <div className="style-icon-certify"></div>
                            </div>
                            <div className="style-community-card">
                              <span>Magic Eden</span>
                            </div>
                          </div>
                        </div>
                        <h3 className="style-title-content">
                          Get in the best NFT marketplace on Solana
                        </h3>
                        <div className="style-rewardsBox-card">
                          <div className="style-container-rewards">
                            <div className="style-content-rewards">
                              <RewardToken typeToken= "usdt" valueToken="2000" />
                              <RewardNft/>
                              <RewardToken typeToken="usdc" valueToken={10000}/>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div className="style-background-card">
                        <div className="style-img-community-circle-image">
                          <img src={magicEden} alt="" />
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div className="style-listItemBox" type-category="Eco System">
                <div className="style-itemBox" target="_blank">
                  <div className="style-container_itemBox">
                    <div className="style-display-itemBox">
                      <div className="style-information-itemBox">
                        <div className="style-content-card">
                          <div className="style-logoBox-card">
                            <div className="style-logo-card">
                              <div className="style-imgbox-card"></div>
                              <div className="style-icon-certify"></div>
                            </div>
                            <div className="style-community-card">
                              <span>Degods</span>
                            </div>
                          </div>
                        </div>
                        <h3 className="style-title-content">
                          Mission Bring Degods Worldwide
                        </h3>
                        <div className="style-rewardsBox-card">
                          <div className="style-container-rewards">
                            <div className="style-content-rewards">
                              <RewardToken typeToken="usdc" valueToken="2000" />
                              <RewardNft/>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div className="style-background-card">
                        <div className="style-img-community-circle-image">
                          <img src={degods} alt="" />
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
