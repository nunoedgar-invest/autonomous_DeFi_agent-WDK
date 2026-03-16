import { Router } from "express"
import { getWalletInfo } from "../controllers/walletController"

const router = Router()

router.get("/", getWalletInfo)

export default router
