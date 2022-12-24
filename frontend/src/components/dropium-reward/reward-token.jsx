import React from "react";
import styled from "styled-components";
import token_usdt from "../../assets/explore/tether-usdt-logo.svg";
import token_usdc from "../../assets/explore/usd-coin-usdc-logo.svg";
import token_sol from "../../assets/explore/solana-sol-logo.svg";

export default function RewardToken({typeToken="usdc"|"usdc",valueToken}) {
    const rewardTypeToken = {
        usdt: `${token_usdt}`,
        usdc: `${token_usdc}`,
        sol: `${token_sol}`
    }
  return (
    <Container>
      <span className="slyle-token-rewards">
        <div className="style-icon-token-rewards">
          <span>
            <span>
              <img src={rewardTypeToken[typeToken]} width="25" height="25" alt="" />
            </span>
            <img src="" alt="" />
          </span>
        </div>
        {valueToken}
      </span>
    </Container>
  );
}

const Container = styled.div`
  .slyle-token-rewards {
    display: flex;
    flex-direction: row;
    align-items: center;
    height: 34px;
    line-height: 34px;
    font-size: 16px;
    white-space: nowrap;
    padding: 0 12px 0 6px;
    background-color: #ff2f61;
    border-radius: 26px;
    margin-right: 8px;
  }
  .style-icon-token-rewards {
    width: 25px;
    height: 25px;
    margin-right: 5px;
  }
`;
