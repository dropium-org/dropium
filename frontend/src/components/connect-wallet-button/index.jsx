import { useWallet } from "@solana/wallet-adapter-react";

import { WalletIcon, useWalletModal } from "@solana/wallet-adapter-react-ui";
import React, {
  useCallback,
  useEffect,
  useMemo,
  useRef,
  useState,
} from "react";
import DropiumButton from "../dropium-button/index.js";
import { WalletConnectButton } from "./wallet-connect-button.js";
import { WalletModalButton } from "./wallet-modal-button.js";

export const ConnectWalletButton = ({ children, ...props }) => {
  const { wallet, publicKey, disconnect } = useWallet();
  const { visible, setVisible } = useWalletModal();
  const [copied, setCopied] = useState(false);
  const [active, setActive] = useState(false);
  const ref = useRef(null);

  const base58 = useMemo(() => publicKey?.toBase58(), [publicKey]);
  const content = useMemo(() => {
    if (children) return children;
    if (!wallet || !base58) return null;
    return base58.slice(0, 4) + ".." + base58.slice(-4);
  }, [children, wallet, base58]);

  const copyAddress = useCallback(async () => {
    if (base58) {
      await navigator.clipboard.writeText(base58);
      setCopied(true);
      setTimeout(() => setCopied(false), 400);
    }
  }, [base58]);

  const openDropdown = useCallback(() => {
    setActive(true);
  }, []);

  const closeDropdown = useCallback(() => {
    setActive(false);
  }, []);

  const openModal = useCallback(() => {
    setVisible(true);
    closeDropdown();
  }, [setVisible, closeDropdown]);

  useEffect(() => {
    const listener = (event) => {
      const node = ref.current;

      // Do nothing if clicking dropdown or its descendants
      if (!node || node.contains(event.target)) return;

      closeDropdown();
    };

    document.addEventListener("mousedown", listener);
    document.addEventListener("touchstart", listener);

    return () => {
      document.removeEventListener("mousedown", listener);
      document.removeEventListener("touchstart", listener);
    };
  }, [ref, closeDropdown]);

  if (!wallet)
    return <WalletModalButton {...props}>{children}</WalletModalButton>;

  if (!base58)
    return <WalletConnectButton {...props}>{children}</WalletConnectButton>;
  return (
    <>
      <div className="wallet-adapter-dropdown">
        <DropiumButton
          hoverEffectDisabled
          aria-expanded={active}
          onButtonClicked={openDropdown}
          borderSide={"both"}
          shadowStyle={{
            backgroundColor: "#60FFE2",
          }}
          style={{ pointerEvents: active ? "none" : "auto", ...props.style, width:"10em" }}
          startIcon={<WalletIcon wallet={wallet} />}
        >
          {content}
        </DropiumButton>
        <ul
          aria-label="dropdown-list"
          className={`wallet-adapter-dropdown-list ${
            active && "wallet-adapter-dropdown-list-active"
          }`}
          ref={ref}
          role="menu"
        >
          <li
            onClick={copyAddress}
            className="wallet-adapter-dropdown-list-item"
            role="menuitem"
          >
            {copied ? "Copied" : "Copy address"}
          </li>
          <li
            onClick={openModal}
            className="wallet-adapter-dropdown-list-item"
            role="menuitem"
          >
            Change wallet
          </li>
          <li
            onClick={disconnect}
            className="wallet-adapter-dropdown-list-item"
            role="menuitem"
          >
            Disconnect
          </li>
        </ul>
      </div>
    </>
  );
};
