import { Request, Response } from "express"
import * as walletService from "../services/walletService"

export async function getWalletInfo(req: Request, res: Response) {

    const wallet = await walletService.getWallet()

    res.json(wallet)
}
