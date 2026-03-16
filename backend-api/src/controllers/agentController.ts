import { Request, Response } from "express"
import * as agentService from "../services/agentService"

export async function getStatus(req: Request, res: Response) {

    const status = await agentService.getAgentStatus()

    res.json(status)
}

export async function startAgent(req: Request, res: Response) {

    const result = await agentService.startAgent()

    res.json(result)
}

export async function stopAgent(req: Request, res: Response) {

    const result = await agentService.stopAgent()

    res.json(result)
}
