import React from "react";
import styled from "styled-components";

export default function RewardNft() {
  return (
    <Container>
      <span className="style-nft-rewards">NFT</span>
    </Container>
  );
}

const Container = styled.div`
.style-nft-rewards {
    display: flex;
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
`;
