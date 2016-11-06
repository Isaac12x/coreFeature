var app = angular.module("app", ["chart.js"]);

app.service("DataService", function () {

    this.boroughs = [
        "Camden",
        "Royal Borough of Greenwich",
        "Hackney",
        "Hammersmith and Fulham",
        "Islington",
        "Royal Borough of Kensington and Chelsea",
        "Lambeth",
        "Lewisham",
        "Southwark",
        "Tower Hamlets",
        "Wandsworth",
        "City of Westminster"
    ];

    this.watsonData = [
        {
            location: "Camden, London",
            boroughData: [0.992541024717, 0.0942619411512, 0.995700559823, 0.482465179389, 0.293729889626]
        },
        {
            location: "Royal Borough of Greenwich, London",
            boroughData: [0.992931832487, 0.0173973195182, 0.991703401564, 0.232890558518, 0.385467100713]
        },
        {
            location: "Hackney, London",
            boroughData: [0.976470983209, 0.0366424898027, 0.986713553464, 0.344429115311, 0.282449620623]
        },
        {
            location: "Hammersmith and Fulham, London",
            boroughData: [0.97711866037, 0.0167021959085, 0.82233616488, 0.175769212926, 0.232959131228]
        },
        {
            location: "Islington, London",
            boroughData: [0.992489908944, 0.0938007105977, 0.995663588764, 0.479111324342, 0.294594435945]
        },
        {
            location: "Royal Borough of Kensington and Chelsea, London",
            boroughData: [0.992151138797, 0.0977839792138, 0.995540271065, 0.488264956039, 0.291734766039]
        },
        {
            location: "Lambeth, London",
            boroughData: [0.992585109084, 0.095735749249, 0.995711029144, 0.481637977847, 0.295574844573]
        },
        {
            location: "Lewisham, London",
            boroughData: [0.97759428236, 0.0159330043121, 0.986839888939, 0.244578099954, 0.249334194474]
        },
        {
            location: "Southwark, London",
            boroughData: [0.992641291221, 0.0969214397756, 0.995776886779, 0.480997509106, 0.299493748715]
        },
        {
            location: "Tower Hamlets, London",
            boroughData: [0.973127794397, 0.0209801540759, 0.992453410471, 0.210764414332, 0.221450932636]
        },
        {
            location: "Wandsworth, London",
            boroughData: [0.979734881487, 0.0790330812613, 0.988759823505, 0.325618774653, 0.367444001181]
        },
        {
            location: "City of Westminster, London",
            boroughData: [0.992641291221, 0.0969214397756, 0.995776886779, 0.480997509106, 0.299493748715]
        }]


})

app.controller("graphCtrl", function ($scope,DataService) {
    $scope.labels = ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Emotional range"];
    $scope.data = [0,0,0,0,0];
    $scope.boroughs = DataService.boroughs;

    $scope.selectOption = function (borough) {

       DataService.watsonData.forEach(function (data) {
           if (data.location === borough + ", London") {
               $scope.data = data.boroughData;
           }
       })
    }


});