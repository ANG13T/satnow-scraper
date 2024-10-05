import calendar
from datetime import datetime
from dateutil import tz
import humanfriendly

# ANSI escape sequences to format output
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BLUE = "\033[0;34m"
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = '\033[1m'
    FADED = '\033[2m'
    UNDERLINE = '\033[4m'
    STRIKETHROUGH = '\033[9m'
    BLINK = "\033[5m"
    ITALIC = "\033[3m"
    NEGATIVE = "\033[7m"
    ENDC = '\033[0m'

def formatStatus(assignment):
    if assignment['submission']['late'] == True:
        return(f"{bcolors.FAIL}✗"+f"{bcolors.ENDC}")
    elif assignment['submission']['workflow_state'] == 'graded':
        return(f"{bcolors.OKGREEN}✓"+f"{bcolors.ENDC}")
    elif assignment['submission']['workflow_state'] == 'submitted':
        return(f"{bcolors.OKBLUE}✓"+f"{bcolors.ENDC}")
    elif assignment['submission']['workflow_state'] == 'pending_review':
        return(f"{bcolors.OKBLUE}🔎"+f"{bcolors.ENDC}")
    elif assignment['submission']['workflow_state'] == 'unsubmitted':
        return(f"{bcolors.WARNING}✗"+f"{bcolors.ENDC}")


def formatCourseScore(score, letter=False):
    if not score:
        return(" -- ")
    elif score >= 90:
        return(f"{(bcolors.OKGREEN)}"+str(score)+f"{bcolors.ENDC}")
    elif score >= 80:
        return(f"{(bcolors.OKBLUE)}"+str(score)+f"{bcolors.ENDC}")
    elif score >= 70:
        return(f"{(bcolors.YELLOW)}"+str(score)+f"{bcolors.ENDC}")
    elif score >= 60:
        return(f"{(bcolors.PURPLE)}"+str(score)+f"{bcolors.ENDC}")
    elif score >= 50:
        return(f"{(bcolors.RED)}"+str(score)+f"{bcolors.ENDC}")
    else:
        return(f"{bcolors.RED}{bcolors.BLINK}"+str(score)+f"{bcolors.ENDC}")





def formatScore(assignment, percentage=False):
    pointsPossible = assignment['points_possible']
    if 'score' not in assignment['submission'].keys():
        return("-/"+str(pointsPossible))
    pointsEarned = assignment['submission']['score']
    score = ''
    # Unscored assignment
    if not pointsEarned:
        return("-/"+str(pointsPossible))
    elif pointsPossible == 0:
            return(f"{bcolors.FADED}"+str(pointsEarned)+f"{bcolors.ENDC}/"+str(pointsPossible))
    else:
        score = float(pointsEarned/pointsPossible)
        percentage = score*100

    if score >= .90:
        if percentage == True:
            scoreString = f"{bcolors.OKGREEN}"+str(percentage)+f"%{bcolors.ENDC}"
        else:
            scoreString = f"{bcolors.OKGREEN}"+str(pointsEarned)+f"{bcolors.ENDC}/"+str(pointsPossible)
    elif score >= .80:
        if percentage == True:
            scoreString = f"{bcolors.OKBLUE}"+str(percentage)+f"%{bcolors.ENDC}"
        else:
            scoreString = f"{bcolors.OKBLUE}"+str(pointsEarned)+f"{bcolors.ENDC}/"+str(pointsPossible)
    elif score >= .70:
        if percentage == True:
            scoreString = f"{bcolors.YELLOW}"+str(percentage)+f"%{bcolors.ENDC}"
        else:
            scoreString = f"{bcolors.YELLOW}"+str(pointsEarned)+f"{bcolors.ENDC}/"+str(pointsPossible)
    elif score >= .60:
        if percentage == True:
            scoreString = f"{bcolors.WARNING}"+str(percentage)+f"%{bcolors.ENDC}"
        else:
            scoreString = f"{bcolors.WARNING}"+str(pointsEarned)+f"{bcolors.ENDC}/"+str(pointsPossible)
    else:
        if percentage == True:
            scoreString = f"{bcolors.BLINK}{bcolors.FAIL}"+str(percentage)+f"%{bcolors.ENDC}"
        else:
            scoreString = f"{bcolors.BLINK}{bcolors.FAIL}"+str(pointsEarned)+f"{bcolors.ENDC}/"+str(pointsPossible)

    return(scoreString)

# convert raw UTC time to localtime.
def formatFromUTC(dueDateUTC):
    utc = datetime.strptime(dueDateUTC, '%Y-%m-%dT%H:%M:%SZ')

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()

    utc = utc.replace(tzinfo=from_zone)

    local = utc.astimezone(to_zone)
    return local

# return a human readable date string from the assignment object.
def formatDueDate(assignment):
    try:
        # Format the input time as UTC
        dueDateRaw = assignment['due_at']

        dueDateObject = formatFromUTC(dueDateRaw) # Actual due date
        todayObject = datetime.now(tz=tz.tzlocal())

        month = calendar.month_abbr[dueDateObject.month]
        day = str(dueDateObject.day)
        hour = str(dueDateObject.hour)
        minute = str(dueDateObject.minute)
        # assigment already submitted
        if assignment['submission']['submitted_at']:
            return(f"{bcolors.STRIKETHROUGH}"+month+" "+day+", "+hour+":"+minute+f"{bcolors.ENDC}")
        # assignment is late
        if assignment['submission']['late']:
            return(f"{bcolors.FAIL}"+month+" "+day+", "+hour+":"+minute+f"{bcolors.ENDC}")
        else:
            daysLeft = abs((dueDateObject - todayObject).days)
            # print(daysLeft)
            if daysLeft >= 7:
                return(f"{bcolors.OKGREEN}"+month+" "+day+", "+hour+":"+minute+f"{bcolors.ENDC}")
            elif daysLeft >= 3:
                return(f"{bcolors.OKBLUE}"+month+" "+day+", "+hour+":"+minute+f"{bcolors.ENDC}")
            elif daysLeft >= 1:
                return(f"{bcolors.WARNING}"+month+" "+day+", "+hour+":"+minute+f"{bcolors.ENDC}")
    except:
        return("--")



# Takes an array of table headers and colors them
def formatHeaders(headers):
    returnArray = []
    for header in headers:
        if header == "Name":
            returnArray.append(f"{bcolors.BLUE}{bcolors.BOLD}"+header+f"{bcolors.ENDC}")
        elif header == "#":
            returnArray.append(f"{bcolors.GREEN}{bcolors.BOLD}"+header+f"{bcolors.ENDC}")
        elif header == "Size":
            returnArray.append(f"{bcolors.PURPLE}{bcolors.BOLD}"+header+f"{bcolors.ENDC}")
        elif header == "Type":
            returnArray.append(f"{bcolors.LIGHT_BLUE}{bcolors.BOLD}"+header+f"{bcolors.ENDC}")
        elif header == "Course":
            returnArray.append(f"{bcolors.CYAN}{bcolors.BOLD}"+header+f"{bcolors.ENDC}")
        elif "Score" in header or "Grade" in header:
            returnArray.append(f"{bcolors.LIGHT_CYAN}{bcolors.BOLD}"+header+f"{bcolors.ENDC}")
        else:
            returnArray.append(f"{bcolors.LIGHT_BLUE}{bcolors.BOLD}"+header+f"{bcolors.ENDC}")

    return(returnArray)

# Takes a filetype from a file and adds an icon
def formatFileType(filetype):
    if filetype == "pdf":
        return(f"{bcolors.LIGHT_GREEN}🗎{bcolors.ENDC} {bcolors.LIGHT_BLUE}PDF{bcolors.ENDC}")
    elif filetype == "video":
        return(f"{bcolors.LIGHT_GREEN}⦾{bcolors.ENDC} {bcolors.LIGHT_BLUE}Video{bcolors.ENDC}")
    elif filetype == "doc":
        return(f"{bcolors.LIGHT_GREEN}🖺{bcolors.ENDC} {bcolors.LIGHT_BLUE}Document{bcolors.ENDC}")
    elif filetype == "image":
        return(f"{bcolors.LIGHT_GREEN}🞖{bcolors.ENDC} {bcolors.LIGHT_BLUE}Image{bcolors.ENDC}")



