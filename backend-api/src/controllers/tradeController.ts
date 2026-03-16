import { Request, Response } from "express"
import * as tradeService from "../services/tradeService"

export async function getTrades(req: Request, res: Response) {

    const trades = await tradeService.getTrades()

    res.json(trades)
}

export async function executeTrade(req: Request, res: Response) {

    const trade = req.body

    const result = await tradeService.executeTrade(trade)

    res.json(result)
}
