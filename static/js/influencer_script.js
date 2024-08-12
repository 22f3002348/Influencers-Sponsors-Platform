document.getElementById("edit-profile").addEventListener("click",function(){
    const editp = document.getElementById("editprofile");
    editp.style.display = "block";
})

document.getElementById("cancelprofile").addEventListener("click",function(){
    const cancelp = document.getElementById("editprofile");
    cancelp.style.display = "none";
})

document.querySelectorAll(".view-campaign").forEach(function(button) {
    button.addEventListener("click", function() {
        const campaign = button.closest(".showrequests");
        const campaigndetails = campaign.querySelector(".showexistingcampaigns");
        if (campaigndetails.style.display === "none" || campaigndetails.style.display === "") {
            campaigndetails.style.display = "block";
        }  
    });
});

document.querySelectorAll(".ad-request").forEach(function(button) {
    button.addEventListener("click", function() {
        const request = button.closest(".showexistingcampaigns");
        const requestdetails = request.querySelector(".Ad-Request");
        if (requestdetails.style.display === "none" || request.style.display === "") {
            requestdetails.style.display = "block";
        }  
    });
});

document.querySelectorAll('.close-campaign').forEach(function(button) {
    button.addEventListener("click", function() {
        const closecampaign = button.closest(".showrequests");
        const closecampaigndetails = closecampaign.querySelector(".showexistingcampaigns");
        closecampaigndetails.style.display ="none";
    });
});

document.querySelectorAll('.cancel-request').forEach(function(button) {
    button.addEventListener('click', function(event) {
        event.preventDefault(); 
        const cancelrequestedit = button.closest('.Ad-Request'); 
        cancelrequestedit.style.display = 'none'; 
    });
});

setTimeout(function() {
    var a = document.getElementById("alert");
    if (a) {
        a.style.display = 'none';
    }
}, 3000);
