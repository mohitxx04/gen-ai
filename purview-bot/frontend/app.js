var app = angular.module("chatApp", []);
 
app.controller("ChatController", function ($scope) {
    $scope.messages = [];
    $scope.userInput = "";
 
    $scope.sendMessage = function () {
        const userMessage = $scope.userInput;
        $scope.messages.push({ user: "You", text: userMessage });
 
        // Simulate a delayed response from the bot
        setTimeout(function () {
            let botResponse;
 
            // Mock bot responses based on user input
            if (userMessage.toLowerCase().includes("hello")) {
                botResponse = "Hi there! How can I assist you today?";
            } else if (userMessage.toLowerCase().includes("alerts")) {
                botResponse = "Here are the top alerts:\n1. Unauthorized Access\n2. Data Breach Attempt.";
            } else if (userMessage.toLowerCase().includes("cybersecurity")) {
                botResponse = "the state of being protected against the criminal or unauthorized use of electronic data, or the measures taken to achieve this."
            }
            else {
                botResponse = "I'm sorry, I don't understand that. Can you rephrase?";
            }
 
            // Push the bot response to the messages array
            $scope.$apply(function () {
                $scope.messages.push({ user: "Bot", text: botResponse });
                $scope.userInput = ""; // Clear input box
            });
        }, 1000); // Simulate 1-second delay
    };
});