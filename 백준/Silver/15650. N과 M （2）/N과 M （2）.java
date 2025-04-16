import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N, R;
    static int[] input, numbers;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        input = new int[N];
        numbers = new int[R];

        for (int i = 0; i < N; i++) {
            input[i] = i + 1;
        }
        comb(0, 0);
        System.out.println(sb);
    }

    private static void comb(int cnt, int start) {
        if (cnt == R) {
            for (int number : numbers) {
                sb.append(number).append(" ");
            }
            sb.append("\n");
            return;
        }
        for (int i = start; i < N; i++) {
            numbers[cnt] = input[i];
            comb(cnt + 1, i + 1);
        }
    }
}