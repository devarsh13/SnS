var myapp = angular.module("myModule",[]);

var dob;
var Day;
var Month;
var Year;
myapp.controller("Main",function($scope){
	var input={
		First_Name:"",
		Last_Name:"",
		Email:"",
		ContactNumber:"",
		Password:"",
		Re_Password:"",
		CityName:"",
		Birthdate:"",
		Gender:"",
		Institute_Name:"",
		Profession_Name:"",
		Image_Link:""
	  };
	input['Date']="";
	input['Month']="";
	input['Year']="";
	$scope.user=input;
	$scope.onMouseLeave_First_Name_Result = "";
	$scope.onMouseLeave_Last_Name_Result = "";
	$scope.onMouseLeave_Email_Result = "";
	$scope.onMouseLeave_ContactNumber_Result = "";
	$scope.onMouseLeave_Password_Result = "";
	$scope.onMouseLeave_Re_Password_Result = "";
	$scope.onMouseLeave_Date_Result = "";
	$scope.onMouseLeave_Month_Result = "";
	$scope.onMouseLeave_Year_Result = "";
	$scope.onMouseLeave_Profession_Name_Result = "";
	$scope.onMouseLeave_Institute_Name_Result = "";
	$scope.onMouseLeave_Image_Link_Result = "";
	$scope.onMouseLeave_First_Name = function ($event) {
	if(input['First_Name']=="")
	{
	$scope.onMouseLeave_First_Name_Result = "First name is required";
	}
	else
	{
	$scope.onMouseLeave_First_Name_Result="";
	}
	};
	$scope.onMouseLeave_Last_Name = function ($event) {
	if(input['Last_Name']=="")
	{
	$scope.onMouseLeave_Last_Name_Result = "Last name is required";
	}
	else
	{
	$scope.onMouseLeave_Last_Name_Result="";
	}
	};
	$scope.onMouseLeave_Email = function ($event) {
	if(input['Email']=="")
	{
	$scope.onMouseLeave_Email_Result = "Email is required";
	}
	else if(!(validateEmail(input['Email'])))
	{
	$scope.onMouseLeave_Email_Result = "Email is not in valid format";;
	}
	else      //Send Email to backend to check email id is already exist or not
	{
	$scope.onMouseLeave_Email_Result="";
	}
	};
	$scope.onMouseLeave_ContactNumber = function ($event) {
	if(input['ContactNumber']=="")
	{
	$scope.onMouseLeave_ContactNumber_Result = "Contact number is required";
	}
	else if(!(isNumber(input['ContactNumber'])))
	{
	$scope.onMouseLeave_ContactNumber_Result = "Invalid number";
	}
	else if((input['ContactNumber'].length!=10))
	{
	$scope.onMouseLeave_ContactNumber_Result = "Contact number should be in 10 digits";
	}
	else
	{
	$scope.onMouseLeave_ContactNumber_Result="";
	}
};
	$scope.onMouseLeave_Password = function ($event) {
	if(input['Password']=="")
	{
	$scope.onMouseLeave_Password_Result = "Password is required";
	}
	else if((input['Password'].length<6))
	{
	$scope.onMouseLeave_Password_Result = "Password length must be at least 6.";
	}
	else
	{
	$scope.onMouseLeave_Password_Result="";
	}
    };
    $scope.onMouseLeave_Re_Password = function ($event) {
	if(input['Re_Password']=="")
	{
	$scope.onMouseLeave_Re_Password_Result = "Confirm Password is required";
	}
	else if((input['Password']!=input['Re_Password']))
	{
	$scope.onMouseLeave_Re_Password_Result = "Confirm Password is not matched ";
	}
	else
	{
	$scope.onMouseLeave_Re_Password_Result="";
	}
    };
    $scope.onMouseLeave_CityName = function ($event) {
	if(input['CityName']=="")
	{
	$scope.onMouseLeave_CityName_Result = "Location is required";
	}
	else
	{
	$scope.onMouseLeave_CityName_Result="";
	}
    };
    $scope.onMouseLeave_Gender = function ($event) {
	if(input['Gender']=="")
	{
	$scope.onMouseLeave_Gender_Result = "Gender is required";
	}
	else
	{
	$scope.onMouseLeave_Gender_Result="";
	}
    };
    $scope.onMouseLeave_Profession_Name = function ($event) {
	if(input['Profession_Name']=="")
	{
	$scope.onMouseLeave_Profession_Name_Result = "Profession is required";
	}
	else
	{
	$scope.onMouseLeave_Profession_Name_Result="";
	}
    };

    $scope.onMouseLeave_Institute_Name = function ($event) {
	if(input['Institute_Name']=="")
	{
	$scope.onMouseLeave_Institute_Name_Result = "Institute is required";
	}
	else
	{
	$scope.onMouseLeave_Institute_Name_Result="";
	}
    };
    $scope.onMouseLeave_Date = function ($event) {
	if(input['Date']=="")
	{
	$scope.onMouseLeave_Date_Result = "Date is required";
	}
	else
	{
	$scope.onMouseLeave_Date_Result="";
	}
    };
    $scope.onMouseLeave_Month = function ($event) {
	if(input['Month']=="")
	{
	$scope.onMouseLeave_Month_Result = "Month is required";
	}
	else
	{
	$scope.onMouseLeave_Month_Result="";
	}
    };
    $scope.onMouseLeave_Year = function ($event) {
	if(input['Year']=="")
	{
	$scope.onMouseLeave_Year_Result = "Year is required";
	}
	else
	{
	$scope.onMouseLeave_Year_Result="";
	}
    };
   $scope.onMouseLeave_Submit = function ($event) {
   	var success=1;
   	if(!$('input[type="file"]').val()) {
   // No file is uploaded, do not submit.
	}
	else
	{
		var files = document.getElementById("image").files;
		var file_name=files[0].name;
	    var split=file_name.split(".");
	    var extenstion = split[split.length-1];
	    if(!(extenstion=="gif" || extenstion=="png" || extenstion=="jpg" || extenstion=="jpeg"))
	    {
	    	$scope.onMouseLeave_Image_Link_Result="It's not an image";
	    	success=0;
	    }
	    else
	    {
	    	$scope.onMouseLeave_Image_Link_Result="";	
	    }
	}
    if(input['First_Name']=="")
    {
    	$scope.onMouseLeave_First_Name_Result = "First name is required";
    	success=0;
    }
    if(input['Last_Name']=="")
    {
    	$scope.onMouseLeave_Last_Name_Result = "Last name is required";
    	success=0;
    }
    if(input['Email']=="")
    {
    	$scope.onMouseLeave_Email_Result = "Email is required";
    	success=0;
    }
    if(input['Password']=="")
    {
    	$scope.onMouseLeave_Password_Result = "Password is required";
    	success=0;
    }
    if(input['Re_Password']=="")
    {
    	$scope.onMouseLeave_Re_Password_Result = "Confirm Password is required";
    	success=0;
    }
    if(input['ContactNumber']=="")
    {
    	$scope.onMouseLeave_ContactNumber_Result = "Contact Number is required";
    	success=0;
    }
    if(input['CityName']=="")
    {
    	$scope.onMouseLeave_CityName_Result = "Location is required";
    	success=0;
    }
    if(input['Gender']=="")
    {
    	$scope.onMouseLeave_Gender_Result = "Gender is required";
    	success=0;
    }
    if(input['Date']=="")
    {
    	$scope.onMouseLeave_Date_Result = "Date is required";
    	success=0;
    }
    if(input['Month']=="")
    {
    	$scope.onMouseLeave_Month_Result = "Month is required";
    	success=0;
    }
    if(input['Year']=="")
    {
    	$scope.onMouseLeave_Year_Result = "Year is required";
    	success=0;
    }
    if(input['Profession_Name']=="")
    {
    	$scope.onMouseLeave_Profession_Name_Result = "Profession name is required";
    	success=0;
    }
    if(input['Institute_Name']=="")
    {
    	$scope.onMouseLeave_Institute_Name_Result = "Institute name is required";
    	success=0;
    }
    if(input['Date']!="" && input['Month']!="" && input['Year']!="")
    {
    	input['Birthdate']=input["Date"]+"/"+input["Month"]+"/"+input["Year"];
    }
    if(success==1)
    {
    	alert("done");
    }

   
    };

});
function validateEmail(email) { 
    var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}
function isNumber(n) {
  return !isNaN(parseFloat(n)) && isFinite(n);
}
