% Simple MATLAB program to pass one piece of the Turing test
% a simple cognitive model for addition of pairs of integers
function result = cognitive_model_addition(int1, int2)
    % Input processing
    num1 = int32(int1);
    num2 = int32(int2);

    % Arithmetic
    result = num1 + num2;

    % Randomness
    if rand() < 0.15
        result = result + randi([-5, 5], 1);
    end

    % Timing
    delay = randi([5, 60], 1);
    tic;
    for j = 1: delay
        for i = 1:1000000000
            i = i;
        end
    end
    total_time = toc;
    fprintf('It took %f seconds to compute the result\n',total_time);
end
