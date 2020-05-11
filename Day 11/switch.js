// It is used to execute code from multiple expressions. It is like if..else..if but more convenient.
var grade = 'B';
var result;
switch (grade) {
  case 'A':
    result = "A grade";
    break;
  case 'B':
    result = "B grade";
    break;
  case 'C':
    result = "C grade";
    break;
  default:
  result = "No grade";
}
document.write(result);
