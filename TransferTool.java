import java.util.HashMap;
public class TransferTool{

  public static void collegeList(){
    // US News T75 2018 https://www.usnews.com/best-graduate-schools/top-science-schools/computer-science-rankings
    HashMap<Integer, String> t75CollegesRank = new HashMap<Integer, String>();
    String[] t75Colleges = new String[]{"Carnegie Mellon University", "Massachusetts Institute of Technology", "Stanford University", "University of California-Berkeley", "University of Illinois-Urbana-Champaign", "Cornell University", "University of Washington", "Georgia Institute of Technology", "Princeton University", "University of Texas-Austin", "California Institute of Technology", "University of Michigan-Ann Arbor", "Columbia University", "University of California-Los Angeles",
      "University of Wisconsin-Madison", "Harvard University", "University of California-San Diego", "University of Maryland-College Park", "University of Pennsylvania", "Purdue University-West Lafayette", "Rice University", "University of Massachusetts-Amherst", "University of Southern California", "Yale University", "Brown University", "Duke University", "Johns Hopkins University", "University of North Carolina-Chapel Hill", "University of Minnesota-Twin Cities",
      "New York University", "Northwestern University", "Ohio State University", "University of California-Irvine", "University of Chicago", "University of Virgina", "Rutgers University-New Brunswick", "University of California-Davis", "University of California-Santa Barbera", "Stony Brook University", "University of Colorado-Boulder", "Virgina Tech", "Arizona State University", "Dartmouth College", "North Carolina State University", "Texas A&M University", "University of Arizona",
      "University of Utah", "Boston University", "Northeastern University", "University of Florida", "University of Pittsburgh", "University of Rochester", "Washington University in St. Louis", "Indiana University-Bloomington", "Michhigan State University", "Rensselaer Polytechnic Institute", "University of California-Santa Cruz", "University of Notre Dame", "Vanderbilt University", "Iowa State University", "University at Buffalo", "University of California-Riverside",
      "University of Illinois-Chicago", "University of Iowa", "University of Oregon", "University of Texas-Dallas", "Case Western Reserve University", "College of William and Mary", "George Mason University", "Oregon State University", "Rochester Institute of Technology", "Syracuse University", "University of Delaware", "Colorado State University", "George Washington University", "Tufts University"};

    for(int i = 1; i < t75Colleges.length; i++){
      t75CollegesRank.put(i, t75Colleges[i]);
    }
    for(Integer rank : t75CollegesRank.keySet()){
      String key = rank.toString();
      String value = t75CollegesRank.get(rank);
      System.out.println(key + ". " + value + "\n");
    }
  }






  public static void main(String[] args) {
    collegeList();
  }
}
