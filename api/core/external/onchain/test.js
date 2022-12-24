const {AccountLayout, TOKEN_PROGRAM_ID,ASSOCIATED_TOKEN_PROGRAM_ID, getAssociatedTokenAddress} = require("@solana/spl-token") ;
const  {clusterApiUrl, Connection, PublicKey} = require("@solana/web3.js");
const { mainModule } = require("process");

const publicKey = new PublicKey("5yPGvUz6JWKjkViGwTCpygJii1rP2xv5yx146ULtBiYq");
const mint = new PublicKey("Ex3R6MrqGU4xoSBBVTy9ukN4cDHoBTih3vacao3bUG6y");



const connection = new Connection(clusterApiUrl('mainnet-beta'));
(async ()=>{
    const associatedAddress = await getAssociatedTokenAddress(
        mint,
        publicKey,
        true,
        TOKEN_PROGRAM_ID,
        ASSOCIATED_TOKEN_PROGRAM_ID,
      );
    
    console.log(associatedAddress.toBase58());
    const tokenAccountInfo = await connection.getParsedAccountInfo(associatedAddress);
    // console.log(tokenAccountInfo)
    console.log((tokenAccountInfo.value?.data ).parsed.info.tokenAmount.amount);
    
})()