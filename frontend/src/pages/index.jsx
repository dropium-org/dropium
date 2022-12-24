import React, { useMemo } from "react";
import "./index.css";
import { Outlet, Route, Router, Routes } from "react-router";
import LandingPage from "./landing-page";

import {
  ConnectionProvider,
  WalletProvider,
} from "@solana/wallet-adapter-react";
import { WalletAdapterNetwork } from "@solana/wallet-adapter-base";
import { PhantomWalletAdapter } from "@solana/wallet-adapter-wallets";
import {
  WalletModalProvider,
  WalletDisconnectButton,
  WalletMultiButton,
} from "@solana/wallet-adapter-react-ui";
import { clusterApiUrl } from "@solana/web3.js";

import DashboardMain from "./dashboard-main";
import Profile from "../components/profile";
import ExploreMain from "../components/explore/explore-main";
import ProfileCreatedQuests from "../components/profile-created-quests-page";
import CreateQuestPage from "../components/profile-create-quest";
import ProfileHeader from "components/header/profile-header";
import ExploreHeader from "components/header/explore-header";
import QuestDetail from "components/quest-detail";

require("@solana/wallet-adapter-react-ui/styles.css");

function App() {
  const network = WalletAdapterNetwork.Devnet;

  // You can also provide a custom RPC endpoint.
  const endpoint = useMemo(() => clusterApiUrl(network), [network]);

  const wallets = useMemo(() => [new PhantomWalletAdapter()], [network]);
  return (
    <ConnectionProvider endpoint={endpoint}>
      <WalletProvider wallets={wallets} autoConnect>
        <WalletModalProvider>
          <Routes>
            <Route path="/app" element={<Outlet />}>
              <Route path="profile/*" element={<ProfileHeader />} />
              <Route path="*" element={<ExploreHeader />} />
            </Route>
          </Routes>
          <Routes>
            {/* {baseUrl}/ */}
            <Route index element={<LandingPage />} />

            <Route path="/app" element={<DashboardMain />}>
              {/* {baseUrl}/app */}
              <Route index element={<ExploreMain />} />

              <Route path="quests" element={<Outlet />}>
                <Route path=":questId" element={<QuestDetail />}></Route>
              </Route>
              <Route path="profile" element={<Profile />}>
                {/* {baseUrl}/app/profile */}
                <Route index element={<ProfileCreatedQuests />} />
                {/* <Route path="my-quests" element={<ProfileCreatedQuests />} /> */}
                <Route path="my-quests">
                  <Route index element={<ProfileCreatedQuests />} />

                  <Route path="create" element={<CreateQuestPage />}></Route>
                </Route>
              </Route>
            </Route>
          </Routes>
        </WalletModalProvider>
      </WalletProvider>
    </ConnectionProvider>
  );
}

export default App;
