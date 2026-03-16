import { renderDashboard } from "./dashboard"
import * as api from "./api"

document.getElementById("startAgent")?.addEventListener("click", async () => {

    await api.startAgent()

    renderDashboard()

})

document.getElementById("stopAgent")?.addEventListener("click", async () => {

    await api.stopAgent()

    renderDashboard()

})

renderDashboard()
