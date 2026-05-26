// ================= CONFIG =================

// ⚠️ Replace with NEW API key (regenerate it)
// let Api_url = "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key=AIzaSyCirE_6EVJbLy1a-c8rT2XC6qy4noV33ng";
let Api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=AIzaSyCirE_6EVJbLy1a-c8rT2XC6qy4noV33ng";


// ================= DOM ELEMENTS =================

let prompt = document.querySelector(".prompt");
let container = document.querySelector(".container");
let chatContainer = document.querySelector(".chat-container");
let btn = document.querySelector(".btn");

let userMessage = "";

// ================= CREATE CHAT BOX =================

function createChatBox(html, className) {
    const div = document.createElement("div");
    div.classList.add(className);
    div.innerHTML = html;
    return div;
}

// ================= SCROLL =================

function scrollToBottom() {
    setTimeout(() => {
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }, 100);
}

// ================= API CALL =================

async function generateApiResponse(aiChatBox) {
    const textElement = aiChatBox.querySelector(".text");

    try {
        const response = await fetch(Api_url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                contents: [
                    {
                        role: "user",
                        parts: [{ text: userMessage }]
                    }
                ]
            })
        });

        const data = await response.json();
        console.log("API RESPONSE:", data);

        if (!response.ok) {
            throw new Error(data?.error?.message || "API Error");
        }

        // ✅ Handle Gemini response safely
        let apiResponse =
            data?.candidates?.[0]?.content?.parts?.[0]?.text ||
            data?.candidates?.[0]?.content?.parts?.map(p => p.text).join(" ");

        // ✅ Fallback
        if (!apiResponse) {
            apiResponse = "No response from AI";
        }

        textElement.innerText = apiResponse;

    } catch (error) {
        console.error("ERROR:", error);
        textElement.innerText = "Error: " + error.message;
    } finally {
        aiChatBox.querySelector(".loading").style.display = "none";
        scrollToBottom();
    }
}

// ================= LOADING UI =================

function showLoading() {
    const html = `
        <div id="img">
            <img src="/static/img/dot_matrix.png" alt="">
        </div>
        <div class="text"></div>
        <img src="/static/img/loading.gif" alt="" height="50" class="loading">
    `;

    let aiChatBox = createChatBox(html, "ai-chat-box");
    chatContainer.appendChild(aiChatBox);

    generateApiResponse(aiChatBox);
    scrollToBottom();
}

// ================= SEND MESSAGE =================

function sendMessage() {
    userMessage = prompt.value.trim();

    if (!userMessage) return;

    container.style.display = "none";

    const html = `
        <div id="img">
            <img src="/static/img/user_2.png" alt="">
        </div>
        <div class="text"></div>
    `;

    let userChatBox = createChatBox(html, "user-chat-box");
    userChatBox.querySelector(".text").innerText = userMessage;

    chatContainer.appendChild(userChatBox);

    prompt.value = "";

    setTimeout(showLoading, 400);
    scrollToBottom();
}

// ================= EVENTS =================

// Button click
btn.addEventListener("click", sendMessage);

// Enter key support
prompt.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
        sendMessage();
    }
});
// test change