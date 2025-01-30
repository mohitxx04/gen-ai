var app = angular.module("chatApp", []);

app.controller("ChatController", function ($scope, $http) {
    $scope.messages = [];
    $scope.userInput = "";

    $scope.sendMessage = function () {
        const userMessage = $scope.userInput;
        $scope.messages.push({ user: "You", text: userMessage });

        // Send request to Flask backend
        $http.post("http://localhost:5000/api/chat", { query: userMessage })
            .then(function (response) {
                const botResponse = response.data.response;
                $scope.messages.push({ user: "Bot", text: botResponse });
                $scope.userInput = "";
            })
            .catch(function (error) {
                console.error("Error fetching response:", error);
                $scope.messages.push({ user: "Bot", text: "Error: Unable to get response." });
            });
    };
});
