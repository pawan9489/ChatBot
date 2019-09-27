
$(document).ready(function () {
    $("#rb-launcher,.rb-close").click(function () {
        $("#rb-chat-frame-container").toggleClass("rb-chat-frame-container-active");
        scrollBottom(container);
    });

    const chatBox = document.getElementById('chatBox');
    const container = document.getElementById('chatbox-container');

    const scrollBottom = element => {
        element.scrollTop = element.scrollHeight - element.clientHeight;
    };

    // const fetch = require('node-fetch');
    const domain = '35.194.94.133';
    // const domain = 'localhost';
    const botURL = `http://${domain}:5005/webhooks/rest/webhook`;
    const userID = Math.floor(Math.random() * Math.floor(9999999));
    const messageToBot = (message, senderID) => ({
        "message": message,
        "sender": `${senderID}`
    });

    const send_a_message = message => fetch(botURL, {
        method: "POST",
        mode: "cors",
        headers: {
            'Content-Type': 'application/json',
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: JSON.stringify(messageToBot(message, userID))
    }).then(response => response.json());

    const enterMessageToInput = event => {
        pumpMessage(event.currentTarget.innerText);
    };
	// <img src="images/tenor.gif" style="height:35px;width:60px;"></img>

	const create_loading_image = () => {
		const img = document.createElement('img');
		img.setAttribute('src', 'images/tenor.gif');
		img.setAttribute('style', 'height:35px;width:60px;border-radius:25px');
		return img;
	};
	
    const frame_a_button = text => {
        // <div class="bubble bubble-inline option theme-border theme-color">
        //     <div>Continue live demo</div>
        // </div>
        const text_div = document.createElement('div');
        text_div.textContent = text;
        const text_wrapper = document.createElement('div');
        text_wrapper.classList.add('bubble');
        text_wrapper.classList.add('bubble-inline');
        text_wrapper.classList.add('option');
        text_wrapper.classList.add('theme-border');
        text_wrapper.classList.add('theme-color');
        text_wrapper.appendChild(text_div);
        text_wrapper.addEventListener("click", enterMessageToInput);
        return text_wrapper;
    };

    // question - String
    // buttons - {"context": "LeaveTypes", "buttons": [{"text": "..."}, {"text": "..."}, {"text": "..."}]} 
    const frame_a_question = (question, buttons) => {
        const avatar_div = document.createElement('div');
        avatar_div.classList.add('avatar');
        const avatar_wrapper = document.createElement('div');
        avatar_wrapper.classList.add('avatar-wrapper');
        avatar_wrapper.classList.add('same-row');
        avatar_wrapper.appendChild(avatar_div);

        const message = document.createElement('div');
        message.textContent = question;
        const message_bubble = document.createElement('div');
        message_bubble.classList.add('bubble-label');
        message_bubble.appendChild(message);

		const time_stamp = document.createElement('span');
		time_stamp.classList.add('comment');
		time_stamp.innerHTML = "&nbsp;";
        const message_border = document.createElement('div');
        message_border.classList.add('bubble');
        message_border.classList.add('no-border');
        message_border.setAttribute('style', 'display: table; direction: unset;');
        const message_bubble_time_wrapper = document.createElement('div');
        message_bubble_time_wrapper.classList.add('same-row');
        message_bubble_time_wrapper.classList.add('question-part');
        message_bubble_time_wrapper.classList.add('text-ltr');
        message_border.appendChild(message_bubble);
        if (buttons) {
            const buttons_bubble = document.createElement('div');
            buttons_bubble.classList.add('bubble-label');
            buttons_bubble.textContent = buttons["context"];
            const option_wrapper = document.createElement('div');
            buttons["buttons"].forEach(button => option_wrapper.appendChild(frame_a_button(button["text"])));
            const button_theme_background = document.createElement('div');
            button_theme_background.classList.add('bubble');
            button_theme_background.classList.add('no-border');
            button_theme_background.classList.add('theme-background');
            button_theme_background.appendChild(buttons_bubble);
            button_theme_background.appendChild(option_wrapper);
            message_border.appendChild(button_theme_background);
        }
        message_bubble_time_wrapper.appendChild(message_border);
		message_bubble_time_wrapper.appendChild(time_stamp);
        const conversation_question = document.createElement('div');
        conversation_question.classList.add('conversation-part');
        conversation_question.classList.add('conversation-part--question');
        conversation_question.appendChild(avatar_wrapper);
        conversation_question.appendChild(message_bubble_time_wrapper);
        return conversation_question;
    };

    const frame_an_answer = answer => {
        const message = document.createElement('div');
        message.classList.add('bubble-label');
        message.textContent = answer;
        const message_bubble_wrapper = document.createElement('div');
        message_bubble_wrapper.classList.add('bubble');
        message_bubble_wrapper.classList.add('no-border');
        message_bubble_wrapper.classList.add('theme-background');
        message_bubble_wrapper.appendChild(message);

		const time_stamp = document.createElement('span');
		time_stamp.classList.add('comment');
        time_stamp.innerHTML = "&nbsp;";
		const answer_text_bubble = document.createElement('div');
        answer_text_bubble.classList.add('answer');
        answer_text_bubble.classList.add('text-ltr');
        const conversation_answer = document.createElement('div');
        conversation_answer.classList.add('conversation-part');
        conversation_answer.classList.add('conversation-part--answer');
        answer_text_bubble.appendChild(message_bubble_wrapper);
        answer_text_bubble.appendChild(time_stamp);
		conversation_answer.appendChild(answer_text_bubble);
		
        return conversation_answer;
    };

    const pumpMessage = message => {
        chatBox.append(frame_an_answer(message));
        $("#textInput").val('');
		const loading_time_out = 500;
        scrollBottom(container);
		chatBox.append(create_loading_image());
        send_a_message(message).then(answers => {
            answers.forEach(answer => {
                // An answer can contain Buttons
                if (answer.buttons) {
                    const buttonsToFeed = answer.buttons.map(button => ({
                        "text": button.payload
                    }));
					setTimeout(() => {
						chatBox.removeChild(chatBox.lastChild);
						chatBox.append(frame_a_question(answer.text, {
							"context": "",
							"buttons": buttonsToFeed
						}));
						scrollBottom(container);
					}, loading_time_out);
                } else {
					setTimeout(() => {
						chatBox.removeChild(chatBox.lastChild);
						chatBox.append(frame_a_question(answer.text));
						scrollBottom(container);
					}, loading_time_out);
                }
                scrollBottom(container);
            });
        });
    };

    chatBox.append(frame_a_question('Hi, I’m Sue, your virtual assistant.'));
    chatBox.append(frame_a_question('What can I do for you today?'));
    // When even an Enter is pressed in the Text box click the submit button
    $("#textInput").keyup(function (event) {
        if (event.keyCode === 13 && $("#textInput").val().trim() !== '') {
            const userRequest = $("#textInput").val().trim();
            pumpMessage(userRequest);
        }
    });

    $("#sendButton").on("click", "button", function () {
        if ($("#textInput").val().trim() !== '') {
            const userRequest = $("#textInput").val().trim();
            pumpMessage(userRequest);
        }
    });

});

// BotsResponse: [
//     {
//         "recipient_id": "default",
//         "text": "Anytime. That's what I'm here for."
//     },
//      {
//          "recipient_id": "49494845",
//          "text": "Can you be more specific about the leave type",
//          "buttons": [
//              {
//                  "payload": "Annual",
//                  "title": "Annual"
//              },
//              {
//                  "payload": "Sick",
//                  "title": "Sick"
//              },
//              {
//                  "payload": "Paid",
//                  "title": "Paid"
//              },
//              {
//                  "payload": "Unpaid",
//                  "title": "Unpaid"
//              }
//          ]
//      }
// ]
