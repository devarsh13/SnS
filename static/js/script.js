var myapp = angular.module("myModule",[]);
var input={
		First_Name:"Chaitanya",
		Last_Name:"Shah",
		Email:"shahchaitu4@gmail.com",
		ContactNumber:"9601559462",
		CityName:"Ahmedabad",
		Birthdate:"11/09/1995",
		Gender:"Male",
		Institute_Name:"DA-IICT",
		Profession_Name:"Student",
		Image_Link:"http://simpleicon.com/wp-content/uploads/user1.svg"
	  };
var dob;
var Day;
var Month;
var Year;
myapp.controller("Main",function($scope){
	dob=input['Birthdate'].split("/");
	Day=dob[0];
	Month=dob[1];
	Year=dob[2];
	$scope.First_Name = input['First_Name'];
	$scope.Last_Name = input['Last_Name'];
	$scope.Email = input['Email'];
	$scope.CityName = input['CityName'];
	$scope.Gender = input['Gender'];
	$scope.ContactNumber=input['ContactNumber'];
	$scope.Day=Day;
	$scope.Month=Month;
	$scope.Year=Year;
	$scope.Profession_Name = input['Profession_Name'];
	$scope.Institute_Name = input['Institute_Name'];
	$scope.onMouseLeave_First_Name_Result = "";
	$scope.onMouseLeave_Last_Name_Result = "";
	$scope.onMouseLeave_Email_Result = "";
	$scope.onMouseLeave_ContactNumber_Result = "";
	$scope.Image_Link=input['Image_Link'];
	$scope.onMouseLeave_First_Name = function ($event) {
	if($scope.First_Name=="")
	{
	$scope.onMouseLeave_First_Name_Result = "First name is required";
	}
	else
	{
	$scope.onMouseLeave_First_Name_Result="";
	input['First_Name']=$scope.First_Name;
	}
    };
	$scope.onMouseLeave_Last_Name = function ($event) {
	if($scope.Last_Name=="")
	{
	$scope.onMouseLeave_Last_Name_Result = "Last name is required";
	}
	else
	{
	$scope.onMouseLeave_Last_Name_Result="";
	input['Last_Name']=$scope.Last_Name;
	}
    };
	$scope.onMouseLeave_Email = function ($event) {
	if($scope.Email=="")
	{
	$scope.onMouseLeave_Email_Result = "Email is required";
	}
	else if(!(validateEmail($scope.Email)))
	{
	$scope.onMouseLeave_Email_Result = "Email is not in valid format";;
	}
	else
	{
	$scope.onMouseLeave_Email_Result="";
	input['Email']=$scope.Email;
	}
    };
	$scope.onMouseLeave_ContactNumber = function ($event) {
	if($scope.ContactNumber=="")
	{
	$scope.onMouseLeave_ContactNumber_Result = "Contact number is required";
	}
	else if(!(isNumber($scope.ContactNumber)))
	{
	$scope.onMouseLeave_ContactNumber_Result = "Invalid number";
	}
	else if(($scope.ContactNumber).length!=10)
	{
	$scope.onMouseLeave_ContactNumber_Result = "Contact number should be in 10 digits";
	}
	else
	{
	$scope.onMouseLeave_ContactNumber="";
	input['ContactNumber']=$scope.ContactNumber;
	}
    };
	
	
	$('.location .dropdown-menu a').on('click', function(){    
		$(".Location").val($(this).html()); 
		input["CityName"]=$(this).html();
		});
	$('.gender .dropdown-menu a').on('click', function(){    
		$(".Gender").val($(this).html()); 
		input["Gender"]=$(this).html();
		});
	$('.day .dropdown-menu a').on('click', function(){    
		$(".Day").val($(this).html()); 
		dob=input['Birthdate'].split("/");
		Day=dob[0];
		Month=dob[1];
		Year=dob[2];
		input["Birthdate"]=$(this).html()+"/"+Month+"/"+Year;
		//alert(input["Birthdate"]);
		});
	$('.month .dropdown-menu a').on('click', function(){    
		$(".Month").val($(this).html());  
		dob=input['Birthdate'].split("/");
		Day=dob[0];
		Month=dob[1];
		Year=dob[2];
		input["Birthdate"]=Day+"/"+$(this).html()+"/"+Year;
		//alert(input["Birthdate"]);
		});
	$('.year .dropdown-menu a').on('click', function(){    
		$(".Year").val($(this).html());  
		dob=input['Birthdate'].split("/");
		Day=dob[0];
		Month=dob[1];
		Year=dob[2];
		input["Birthdate"]=Day+"/"+Month+"/"+$(this).html();
		//alert(input["Birthdate"]);
		});
	$('.profession .dropdown-menu a').on('click', function(){    
		$('.profession .dropdown-toggle').html($(this).html() + '<span class="caret"></span>'); 
		input["Profession_Name"]=$(this).html();
		});
	$('.institute .dropdown-menu a').on('click', function(){    
		$('.institute .dropdown-toggle').html($(this).html() + '<span class="caret"></span>'); 
		input["Institute_Name"]=$(this).html();
		});
	$scope.onMouseClick_Changes = function ($event) {
		if($scope.onMouseLeave_First_Name_Result=="" && $scope.onMouseLeave_Last_Name_Result=="" && $scope.onMouseLeave_Email_Result=="" && $scope.onMouseLeave_ContactNumber_Result=="")
			{
			alert(input);
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