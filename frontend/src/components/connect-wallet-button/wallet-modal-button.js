import React, { useCallback } from 'react';
import {
    useWalletModal
} from "@solana/wallet-adapter-react-ui";
import DropiumButton from '../dropium-button';

export const WalletModalButton = ({ children = 'Select Wallet', onClick, ...props }) => {
    const { visible, setVisible } = useWalletModal();

    const handleClick = useCallback(
        (event) => {
            console.log(onClick,event.defaultPrevented)
            if (onClick) onClick(event);
            
            setVisible(!visible);
        },
        [onClick, setVisible, visible]
    );
    return (
        <DropiumButton
            hoverEffectDisabled
            onButtonClicked={handleClick}
            borderSide={"both"}
            shadowStyle={{
                backgroundColor: "#60FFE2",
            }}
            {...props}
        >
            {children}
        </DropiumButton>
    );
};
