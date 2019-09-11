
extern crate reqwest;

fn main(){
// Building the URL
fn game_day_url(level: &str, year: &str, month: &str, day: &str) -> String{

    String::from("http://gd2.mlb.com/components/game/") + level
                    + "/year_" + year
                    + "/month_" + month
                    + "/day_" + day
}

// Extracting the Game Links into a List of Links
fn game_day_links (url: &str) -> Vec<String> {
    // sends out request to network that will return a Result
    let resp = reqwest::get(url);
    // Check for response
    if resp.is_ok(){
        //  unwrap and get the text
        let links = resp.unwrap().text().unwrap_or("".to_string());
        // split all phrases in <li> web tag
        links.split("<li>")
            // only want those phrases that contain gid (gameday id?)
            .filter(|line| line.contains("gid_"))
            // takes each item and maps it to a new value
            .map(|line| url.to_string().clone() + "/"
            // split into sub list when we see a separator ( < or >)
            + line.split(|c| c == '>' || c == '<')
            // take third item
            .collect::<Vec<&str>>()[2]
            // trim any whitespace
            .trim()
        )
        .collect::<Vec<String>>()
    }
    else {
        vec![]
    }
}

let url = game_day_url("mlb", "2018", "06", "10");
let games = game_day_links(&url);

dbg!(games);
}
